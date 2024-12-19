import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance, PointStruct

load_dotenv()

VDB_HOST = os.environ.get("VDB_HOST", "localhost")
VDB_PORT = os.environ.get("VDB_PORT", "6379")


class QdrantSessionClient:
    def __init__(self):
        self.client = QdrantClient(host=VDB_HOST, port=VDB_PORT, prefer_grpc=True)


    def is_alive(self) -> bool:
        try:
            print(self.client.get_collections())
            return True
        except:
            return False
        
        
    def create_collection(self, collection_name: str, vector_size: int, distance: Distance | None = Distance.COSINE) -> None:
        self.client.recreate_collection(
            collection_name=collection_name,
            vectors_config=VectorParams(
                size=vector_size,
                distance=distance,
            )
            
        )
    
        
    def upsert_points(self, collection_name: str, chunks: list[any], vectors: list[any]):
        self.client.upsert(
            collection_name=collection_name,
            points=[
                PointStruct(
                    id=idx,
                    vector=vector,
                    payload={"chunk": chunk}
                )
                for idx, (vector, chunk) in enumerate(zip(vectors, chunks))
            ]
        )
        return self.client.count(collection_name=collection_name)
    
    
    
    def search(self, collection_name: str, query_vector: list[any], top_k: int) -> list[any]:
        results = self.client.search(
            collection_name=collection_name,
            query_vector=query_vector,
            limit=top_k
        )
        return results