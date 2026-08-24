import json
import math
import re
from pathlib import Path

from langchain_core.documents import Document


class VectorRetriever:

    def __init__(self):
        self.index = self._load_index()
        self._doc_freq = self._build_doc_freq()

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

    def _build_doc_freq(self):
        """How many chunks each word appears in — used to down-weight
        common filler words ('is', 'what') and up-weight rare, specific
        words ('turing', 'relational') during scoring."""
        doc_freq = {}
        for item in self.index:
            terms = set(re.findall(r"[a-z0-9]+", item.get("page_content", "").lower()))
            for term in terms:
                doc_freq[term] = doc_freq.get(term, 0) + 1
        return doc_freq

    def _idf(self, term):
        n = len(self.index) or 1
        df = self._doc_freq.get(term, 0)
        return math.log((n + 1) / (df + 1)) + 1

    def retrieve(self, query, k=5):
        query_terms = set(re.findall(r"[a-z0-9]+", query.lower()))
        ranked = []
        for item in self.index:
            content = item.get("page_content", "")
            content_terms = set(re.findall(r"[a-z0-9]+", content.lower()))
            matched = query_terms & content_terms
            if not matched:
                continue
            score = sum(self._idf(term) for term in matched)
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