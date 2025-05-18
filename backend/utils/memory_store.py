import chromadb
from chromadb.config import Settings
from datetime import datetime

client = chromadb.Client(Settings(persist_directory="./data/chroma", anonymized_telemetry=False))
insight_collection = client.get_or_create_collection("insights")
log_collection = client.get_or_create_collection("logs")

def store_insight(text, metadata):
    insight_collection.add(documents=[str(text)], metadatas=[metadata], ids=[metadata["id"]])

def search_insights(query, k=5):
    results = insight_collection.query(query_texts=[query], n_results=k)
    return results["documents"][0] if results["documents"] else []

def log_agent_run(agent_name, output):
    log_collection.add(
        documents=[str(output)],  # Ensure output is stored as string
        metadatas=[{"agent": agent_name, "timestamp": datetime.now().isoformat()}],
        ids=[f"{agent_name}_{datetime.now().isoformat()}"]
    )
