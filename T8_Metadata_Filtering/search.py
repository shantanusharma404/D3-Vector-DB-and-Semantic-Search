import chromadb

# Connect to ChromaDB
client = chromadb.PersistentClient(
    path="./chroma_db"
)

# Load collection
collection = client.get_collection(
    name="metadata_demo"
)

# =========================
# FILTER 1
# Category = AI
# =========================

print("\nFILTER 1: Category = AI")
print("=" * 50)

results = collection.query(
    query_texts=["learning"],
    n_results=3,
    where={
        "category": "AI"
    }
)

for doc in results["documents"][0]:
    print(doc)

# =========================
# FILTER 2
# Category = Sports
# =========================

print("\nFILTER 2: Category = Sports")
print("=" * 50)

results = collection.query(
    query_texts=["game"],
    n_results=3,
    where={
        "category": "Sports"
    }
)

for doc in results["documents"][0]:
    print(doc)

# =========================
# FILTER 3
# Category = AI
# AND
# Difficulty = Beginner
# =========================

print("\nFILTER 3: Category = AI AND Difficulty = Beginner")
print("=" * 50)

results = collection.query(
    query_texts=["artificial intelligence"],
    n_results=3,
    where={
        "$and": [
            {"category": "AI"},
            {"difficulty": "Beginner"}
        ]
    }
)

for doc in results["documents"][0]:
    print(doc)