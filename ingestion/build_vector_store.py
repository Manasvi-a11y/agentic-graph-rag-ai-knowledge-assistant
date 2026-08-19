import json
from pathlib import Path

from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter


def main():
    index_path = Path("vector_db/flat_index.json")
    if index_path.exists() and index_path.stat().st_size > 0:
        print(f"[INFO] Text index already exists at {index_path}; skipping ingestion.")
        return

    documents = DocumentLoader("knowledge_base").load_documents()
    if not documents:
        raise RuntimeError("No documents found in knowledge_base.")

    chunks = DocumentSplitter().split_documents(documents)
    index_path.parent.mkdir(parents=True, exist_ok=True)
    index_path.write_text(
        json.dumps(
            [
                {"page_content": chunk.page_content, "metadata": chunk.metadata}
                for chunk in chunks
                if chunk.page_content and chunk.page_content.strip()
            ],
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    print(f"[OK] Text index ready with {len(chunks)} chunks.")


if __name__ == "__main__":
    main()