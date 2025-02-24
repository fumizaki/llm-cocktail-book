import os
from dotenv import load_dotenv
from neo4j import GraphDatabase

load_dotenv()

GRAPH_USER = os.environ.get("GRAPH_USER", "graph")
GRAPH_PASSWORD = os.environ.get("GRAPH_PASSWORD", "graph")
GRAPH_HOST = os.environ.get("GRAPH_HOST", "neo4j")
GRAPH_PORT = os.environ.get("GRAPH_PORT", "7687")

driver = GraphDatabase.driver(uri=f'bolt://{GRAPH_HOST}:{GRAPH_PORT}', auth=(GRAPH_USER, GRAPH_PASSWORD))

def get_neo4j_session():
    try:
        session = driver.session()
        yield session
    finally:
        session.close()


