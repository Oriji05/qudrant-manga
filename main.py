from fastapi import FastAPI
from qdrant_client import QdrantClient
from qdrant_client.models import *
from src.Converter import Converter
import json


app = FastAPI()

# Connessione al database Qdrant locale
qdrant = QdrantClient("localhost", port=6333)

COLLECTION_NAME = "mangas"

@app.get("/search")
def search(name, tlimit):
    converter = Converter(name)

    results = qdrant.query_points(
    collection_name=COLLECTION_NAME,
    query=list(converter.execute()),
    with_payload=True,
    limit=tlimit
    ).points

    return {"results": [hit.dict() for hit in results]}

@app.get("/searchSimilarById")
def search(id : int, tlimit):

    manga = qdrant.retrieve(COLLECTION_NAME, ids=[id],with_vectors=True)
    results = qdrant.query_points(
        COLLECTION_NAME,
        query=manga[0].vector,
        limit=tlimit

    ).points
    return {"results": [hit.model_dump() if hasattr(hit, "model_dump") else hit for hit in results]}



if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
