from langchain_huggingface import HuggingFaceEmbeddings

from config import settings


class EmbeddingModel:

    def __init__(self):

        self.model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        )

    def get_embedding_model(self):

        return self.model