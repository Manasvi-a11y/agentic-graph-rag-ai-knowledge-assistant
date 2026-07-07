from pathlib import Path
from typing import List

from langchain.schema import Document

from retrieval.vector_store import load_vector_store


def query_store(query_text: str, persist_directory: Path, k: int = 4) -> List[Document]:
    db = load_vector_store(persist_directory)
    return db.similarity_search(query_text, k=k)


if __name__ == "__main__":
    persist_dir = Path(__file__).resolve().parent.parent / "vector_db"
    query_text = "Explain the basics of Python programming."
    docs = query_store(query_text, persist_dir)
    for i, doc in enumerate(docs, 1):
        print(f"--- Result {i} ---")
        print(doc.page_content[:400].strip())
        print("metadata:", doc.metadata)
        print()
