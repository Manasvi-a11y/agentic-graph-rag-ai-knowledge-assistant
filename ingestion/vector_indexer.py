from langchain_chroma import Chroma

from config import settings
from ingestion.embedding import EmbeddingModel


class VectorIndexer:

    def __init__(self):

        self.embedding_model = (
            EmbeddingModel()
            .get_embedding_model()
        )

    def create_vector_store(
        self,
        chunks
    ):

        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=self.embedding_model,
            persist_directory=settings.CHROMA_DB_PATH
        )

        print("Vector Database Created Successfully")

        return vectordb