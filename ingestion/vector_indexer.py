from pathlib import Path

from langchain_chroma import Chroma

from config import settings
from ingestion.embedding import EmbeddingModel


class VectorIndexer:

    def __init__(self):
        self.embedding_model = EmbeddingModel().get_embedding_model()
        self.persist_dir = str(Path(settings.CHROMA_DB_PATH).resolve())
        Path(self.persist_dir).mkdir(parents=True, exist_ok=True)

    def _normalize_text(self, value):
        if value is None:
            return ""

        if isinstance(value, bytes):
            return value.decode("utf-8", errors="replace")

        if isinstance(value, (list, tuple, set)):
            parts = [self._normalize_text(item) for item in value if item is not None]
            return " ".join(part for part in parts if part)

        if isinstance(value, dict):
            parts = [self._normalize_text(item) for item in value.values() if item is not None]
            return " ".join(part for part in parts if part)

        return str(value)

    def _sanitize_chunks(self, chunks):
        cleaned = []
        for index, chunk in enumerate(chunks or []):
            if chunk is None:
                continue

            content = self._normalize_text(getattr(chunk, "page_content", ""))
            content = " ".join(content.split())
            if not content:
                continue

            chunk.page_content = content
            if not isinstance(chunk.metadata, dict):
                chunk.metadata = {}
            chunk.metadata.setdefault("chunk_id", index)
            cleaned.append(chunk)

        return cleaned

    def create_vector_store(self, chunks):
        cleaned_chunks = self._sanitize_chunks(chunks)
        if not cleaned_chunks:
            raise ValueError("No valid document chunks were produced for vector indexing.")

        vectordb = Chroma.from_documents(
            documents=cleaned_chunks,
            embedding=self.embedding_model,
            persist_directory=self.persist_dir,
        )

        print(f"Vector Database Created Successfully at {self.persist_dir}")
        return vectordb