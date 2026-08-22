import json
from pathlib import Path

from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter


def _clean_text(text: str) -> str:
    """Strip characters (e.g. lone surrogates from broken PDF fonts/icons)
    that can't be safely round-tripped through UTF-8."""
    if not isinstance(text, str):
        return text
    return text.encode("utf-8", errors="ignore").decode("utf-8", errors="ignore")


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

    records = []
    skipped = 0
    for chunk in chunks:
        content = _clean_text(chunk.page_content)
        if not content or not content.strip():
            skipped += 1
            continue
        clean_metadata = {
            key: (_clean_text(value) if isinstance(value, str) else value)
            for key, value in (chunk.metadata or {}).items()
        }
        records.append({"page_content": content, "metadata": clean_metadata})

    if skipped:
        print(f"[INFO] Skipped {skipped} chunks that were empty after cleaning.")

    index_path.write_text(
        json.dumps(records, ensure_ascii=False),
        encoding="utf-8",
    )
    print(f"[OK] Text index ready with {len(records)} chunks.")


if __name__ == "__main__":
    main()