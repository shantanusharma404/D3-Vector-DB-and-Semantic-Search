from sentence_transformers import SentenceTransformer
from documents import documents
import numpy as np

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

embeddings = model.encode(documents)

print("Embedding Shape:")
print(embeddings.shape)

np.save(
    "embeddings.npy",
    embeddings
)

print("Embeddings Saved")