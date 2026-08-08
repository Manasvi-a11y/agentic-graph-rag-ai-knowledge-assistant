from functools import lru_cache

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central configuration for the project.
    All environment variables are loaded from .env.
    """

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )

    # ==========================
    # LLM
    # ==========================

    GROQ_API_KEY: str = Field(...)
    GROQ_MODEL: str = "llama-3.3-70b-versatile"

    # ==========================
    # Embedding Model
    # ==========================

    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"

    # ==========================
    # Chroma
    # ==========================

    CHROMA_DB_PATH: str = "./vector_db"

    # ==========================
    # Neo4j
    # ==========================

    NEO4J_URI: str
    NEO4J_USERNAME: str
    NEO4J_PASSWORD: str

    # ==========================
    # Retrieval
    # ==========================

    TOP_K: int = 5

    CHUNK_SIZE: int = 800

    CHUNK_OVERLAP: int = 150

    # ==========================
    # Project
    # ==========================

    PROJECT_NAME: str = "Agentic Graph RAG"

    DEBUG: bool = True


@lru_cache
def get_settings():
    return Settings()


settings = get_settings()