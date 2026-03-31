from qdrant_client import QdrantClient, models
import uuid

#initialize the qdrant client
def get_qdrant_client(url: str, api_key: str) -> QdrantClient:
    return QdrantClient(url=url, api_key=api_key)

# create a collection in qdrant
def create_collection(client: QdrantClient, collection_name: str, vector_size: int):
