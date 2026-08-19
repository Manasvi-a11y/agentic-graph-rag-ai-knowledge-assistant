import json
import re
from pathlib import Path

from langchain_core.documents import Document


class VectorRetriever:

    def __init__(self):
        self.index = self._load_index()

    @staticmethod
    def _load_index():
        index_path = Path("vector_db/flat_index.json")
        if not index_path.exists():
            print("[WARN] Text index is missing; run the Railway build command.")
            return []
        try:
            return json.loads(index_path.read_text(encoding="utf-8"))
        except Exception as error:
            print(f"[WARN] Could not load text index: {error}")
            return []

    def retrieve(self, query, k=5):
        query_terms = set(re.findall(r"[a-z0-9]+", query.lower()))
        ranked = []
        for item in self.index:
            content = item.get("page_content", "")
            content_terms = set(re.findall(r"[a-z0-9]+", content.lower()))
            score = len(query_terms & content_terms)
            if score:
                ranked.append((score, item))
        ranked.sort(key=lambda result: result[0], reverse=True)
        docs = [
            Document(page_content=item["page_content"], metadata=item.get("metadata", {}))
            for _, item in ranked[:k]
        ]

        print("\n==========================")
        print("QUERY:", query)
        print("Retrieved:", len(docs))

        for i, doc in enumerate(docs):
            print(f"\nDocument {i + 1}")
            print(doc.metadata)
            print(doc.page_content[:300])

        print("==========================\n")

        return docs