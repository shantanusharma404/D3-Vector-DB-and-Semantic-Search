import chromadb

client = chromadb.PersistentClient(
    path="./chroma_db"
)

collection = client.get_collection(
    name="learning_docs"
)

query = input("Enter your query: ")

results = collection.query(
    query_texts=[query],
    n_results=3
)

print("\nTop Matches:\n")

for i, doc in enumerate(results["documents"][0], start=1):
    print(f"{i}. {doc}")