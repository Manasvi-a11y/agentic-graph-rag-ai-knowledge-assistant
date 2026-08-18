from pathlib import Path

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

from config import settings
from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from ingestion.vector_indexer import VectorIndexer


class VectorRetriever:

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={"device": "cpu"},
            encode_kwargs={"normalize_embeddings": True},
        )

        self.db = Chroma(
            persist_directory=settings.CHROMA_DB_PATH,
            embedding_function=self.embeddings,
        )

        self.ensure_vector_store()

    def ensure_vector_store(self):
        try:
            count = self.db._collection.count()
        except Exception:
            count = 0

        if count > 0:
            return

        knowledge_dir = Path("knowledge_base")
        if not knowledge_dir.exists():
            return

        print("[INFO] Chroma vector store is empty. Building it from the local knowledge base...")

        documents = DocumentLoader(str(knowledge_dir)).load_documents()
        if not documents:
            print("[WARN] No documents found in knowledge_base; skipping vector initialization.")
            return

        chunks = DocumentSplitter().split_documents(documents)
        VectorIndexer().create_vector_store(chunks)

        self.db = Chroma(
            persist_directory=settings.CHROMA_DB_PATH,
            embedding_function=self.embeddings,
        )

    def retrieve(self, query, k=5):
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