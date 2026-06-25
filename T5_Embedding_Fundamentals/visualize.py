import numpy as np
import umap
import matplotlib.pyplot as plt

embeddings = np.load("embeddings.npy")

labels = (
    ["AI"] * 20 +
    ["Sports"] * 20 +
    ["Finance"] * 20
)

reducer = umap.UMAP(
    n_components=2,
    random_state=42
)

embedding_2d = reducer.fit_transform(
    embeddings
)

colors = {
    "AI": "blue",
    "Sports": "green",
    "Finance": "red"
}

plt.figure(figsize=(10,7))

for category in colors:

    idx = [
        i for i, label
        in enumerate(labels)
        if label == category
    ]

    plt.scatter(
        embedding_2d[idx, 0],
        embedding_2d[idx, 1],
        label=category
    )

plt.title(
    "Document Embedding Visualization using UMAP"
)

plt.xlabel("UMAP Dimension 1")
plt.ylabel("UMAP Dimension 2")

plt.legend()

plt.savefig(
    "embedding_visualization.png"
)

plt.show()