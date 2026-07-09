from pathlib import Path

from ingestion.loader import load_documents
from ingestion.splitter import split_documents
from retrieval.vector_store import build_vector_store


def main() -> None:
    repo_root = Path(__file__).resolve().parent
    data_dir = repo_root / "knowledge_base"
    persist_dir = repo_root / "vector_db"

    print("Loading PDF documents from:", data_dir)
    documents = load_documents(data_dir)
    print(f"Loaded {len(documents)} documents from PDFs.")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)
    print(f"Created {len(chunks)} text chunks.")

    print("Building Chroma vector store...")
    build_vector_store(chunks, persist_dir)
    print("Vector store persisted to:", persist_dir)


if __name__ == "__main__":
    main()
