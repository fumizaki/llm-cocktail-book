import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

VECTOR_HOST = os.environ.get("VECTOR_HOST", "localhost")
VECTOR_PORT = os.environ.get("VECTOR_PORT", "6379")

def get_qdrant_session() -> QdrantClient:
    try:
        return QdrantClient(host=VECTOR_HOST, port=VECTOR_PORT, prefer_grpc=True)
    except:
        raise