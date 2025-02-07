import os
from dotenv import load_dotenv
from qdrant_client import QdrantClient

load_dotenv()

VDB_HOST = os.environ.get("VDB_HOST", "localhost")
VDB_PORT = os.environ.get("VDB_PORT", "6379")

def get_qdrant_session() -> QdrantClient:
    try:
        return QdrantClient(host=VDB_HOST, port=VDB_PORT, prefer_grpc=True)
    except:
        raise