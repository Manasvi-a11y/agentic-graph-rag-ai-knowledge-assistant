from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import settings
from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from ingestion.vector_indexer import VectorIndexer


class VectorRetriever:

    def __init__(self):
        self.embeddings = None
        self.db = Chroma(persist_directory=settings.CHROMA_DB_PATH)

        if self.db._collection.count() > 0:
            self.embeddings = HuggingFaceEmbeddings(
                model_name=settings.EMBEDDING_MODEL,
                model_kwargs={"device": "cpu"},
                encode_kwargs={"normalize_embeddings": True},
            )
            self.db = Chroma(
                persist_directory=settings.CHROMA_DB_PATH,
                embedding_function=self.embeddings,
            )
        else:
            self.ensure_vector_store()

    def ensure_vector_store(self):
        try:
            count = self.db._collection.count()
        except Exception:
            count = 0

        if count > 0:
            return

        print("[WARN] Chroma vector store is empty; skipping request-time PDF ingestion.")

    def retrieve(self, query, k=5):
        if self.db._collection.count() == 0:
            return []

        docs = self.db.similarity_search(query, k=k)

        print("\n==========================")
        print("QUERY:", query)
        print("Retrieved:", len(docs))

        for i, doc in enumerate(docs):
            print(f"\nDocument {i + 1}")
            print(doc.metadata)
            print(doc.page_content[:300])

        print("==========================\n")

        return docs