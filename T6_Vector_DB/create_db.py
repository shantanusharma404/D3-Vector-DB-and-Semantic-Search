import chromadb
from documents import documents

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_or_create_collection(
    name="learning_docs"
)

ids = [f"doc_{i}" for i in range(len(documents))]

collection.add(
    documents=documents,
    ids=ids
)

print(f"{len(documents)} documents added successfully!")