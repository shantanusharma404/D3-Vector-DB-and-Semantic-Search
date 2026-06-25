import chromadb
from documents import documents, metadatas

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="metadata_demo"
)

ids = [
    "doc1",
    "doc2",
    "doc3",
    "doc4",
    "doc5",
    "doc6"
]

collection.add(
    documents=documents,
    metadatas=metadatas,
    ids=ids
)

print("Documents and metadata added successfully!")