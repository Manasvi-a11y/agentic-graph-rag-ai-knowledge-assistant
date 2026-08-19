from pathlib import Path

from langchain_chroma import Chroma

from config import settings
from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from ingestion.vector_indexer import VectorIndexer


def main():
    persist_dir = Path(settings.CHROMA_DB_PATH)
    persist_dir.mkdir(parents=True, exist_ok=True)

    try:
        existing = Chroma(persist_directory=str(persist_dir))._collection.count()
    except Exception:
        existing = 0

    if existing > 0:
        print(f"[INFO] Chroma index already contains {existing} documents; skipping ingestion.")
        return

    documents = DocumentLoader("knowledge_base").load_documents()
    if not documents:
        raise RuntimeError("No documents found in knowledge_base.")

    chunks = DocumentSplitter().split_documents(documents)
    VectorIndexer().create_vector_store(chunks)
    print(f"[OK] Vector index ready with {len(chunks)} chunks.")


if __name__ == "__main__":
    main()