from qdrant_client import QdrantClient
from qdrant_client.models import Distance, VectorParams
from qdrant_client.models import PointStruct
from src.Converter import Converter
import json

with open("dataset/mangas.json", "r", encoding="utf-8") as f:
    data = json.load(f)


client = QdrantClient(url="http://localhost:6333")
try:
    client.create_collection(
        collection_name="mangas",
        vectors_config=VectorParams(size=384, distance=Distance.DOT),
    )
except Exception as e:
    print(e)


for manga in data:
    
    try:
        
        converter = Converter(manga['synopsis'])
        mVector = list(converter.execute())
        operation_info = client.upsert(
        collection_name="mangas",
        wait=True,
        points=[
            PointStruct(
                id = manga['id'], 
                vector= mVector,
                payload={"name": manga['name'] ,"synopsis": converter.getText()}
            )
            ]
        )
    
    except Exception as e:
        print(f"{e}")
    print(manga['id'])





print(operation_info)


