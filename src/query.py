from qdrant_client import QdrantClient
client = QdrantClient(url="http://localhost:6333")

search_result = client.query_points(
    collection_name="test_collection",
    query=[-0.0518574,0.056877203,-0.07024913,0.019524142],
    with_payload=True,
    limit=1
).points

print(search_result)