from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import (
    cosine_similarity,
    euclidean_distances
)
import numpy as np

# Load embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

# Query
query = "Explain Artificial Intelligence"

# Sample documents
documents = [
    "What is Machine Learning?",
    "Cricket is a bat and ball sport.",
    "Stocks represent ownership in a company.",
    "What is Deep Learning?",
    "How do Neural Networks work?"
]

# Generate embeddings
query_embedding = model.encode([query])
doc_embeddings = model.encode(documents)

# =========================
# COSINE SIMILARITY
# =========================

print("\nCOSINE SIMILARITY")
print("=" * 50)

cos_scores = cosine_similarity(
    query_embedding,
    doc_embeddings
)[0]

for doc, score in zip(documents, cos_scores):
    print(f"{score:.4f} | {doc}")

# =========================
# DOT PRODUCT
# =========================

print("\nDOT PRODUCT")
print("=" * 50)

dot_scores = np.dot(
    doc_embeddings,
    query_embedding.T
).flatten()

for doc, score in zip(documents, dot_scores):
    print(f"{score:.4f} | {doc}")

# =========================
# EUCLIDEAN DISTANCE
# =========================

print("\nEUCLIDEAN DISTANCE")
print("=" * 50)

euclidean_scores = euclidean_distances(
    query_embedding,
    doc_embeddings
)[0]

for doc, score in zip(documents, euclidean_scores):
    print(f"{score:.4f} | {doc}")