import json
from pathlib import Path

import numpy as np
from langchain_core.documents import Document
from sentence_transformers import SentenceTransformer

EMBEDDING_MODEL = "all-MiniLM-L6-v2"


class VectorRetriever:

    def __init__(self):
        self.index = self._load_index()
        self.embeddings = self._load_embeddings()
        self.model = SentenceTransformer(EMBEDDING_MODEL) if self.index else None

    @staticmethod
    def _load_index():
        index_path = Path("vector_db/flat_index.json")
        if not index_path.exists():
            print("[WARN] Text index is missing; run the Railway build command.")
            return []
        try:
            index = json.loads(index_path.read_text(encoding="utf-8"))
            print(f"[INFO] Loaded text index with {len(index)} chunks.")
            return index
        except Exception as error:
            print(f"[WARN] Could not load text index: {error}")
            return []

    @staticmethod
    def _load_embeddings():
        embeddings_path = Path("vector_db/embeddings.npy")
        if not embeddings_path.exists():
            print("[WARN] Embeddings file is missing; run the Railway build command.")
            return None
        try:
            embeddings = np.load(embeddings_path)
            print(f"[INFO] Loaded embeddings with shape {embeddings.shape}.")
            return embeddings
        except Exception as error:
            print(f"[WARN] Could not load embeddings: {error}")
            return None

    def retrieve(self, query, k=5):
        if not self.index or self.embeddings is None or self.model is None:
            return []

        query_vector = self.model.encode(
            [query], normalize_embeddings=True
        ).astype("float32")[0]

        scores = self.embeddings @ query_vector
        top_k_idx = np.argsort(scores)[::-1][:k]

        docs = [
            Document(
                page_content=self.index[i]["page_content"],
                metadata=self.index[i].get("metadata", {}),
            )
            for i in top_k_idx
        ]

        print("\n==========================")
        print("QUERY:", query)
        print("Retrieved:", len(docs))
        for i, doc in enumerate(docs):
            print(f"\nDocument {i + 1} (score={scores[top_k_idx[i]]:.3f})")
            print(doc.metadata)
            print(doc.page_content[:300])
        print("==========================\n")

        return docs