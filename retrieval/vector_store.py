from pathlib import Path
from typing import List

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.schema import Document


def build_vector_store(documents: List[Document], persist_directory: Path, collection_name: str = "knowledge_base") -> Chroma:
    persist_directory = Path(persist_directory)
    persist_directory.mkdir(parents=True, exist_ok=True)

    embeddings = OpenAIEmbeddings()
    db = Chroma.from_documents(
        documents,
        embeddings,
        persist_directory=str(persist_directory),
        collection_name=collection_name,
    )
    db.persist()
    return db


def load_vector_store(persist_directory: Path, collection_name: str = "knowledge_base") -> Chroma:
    embeddings = OpenAIEmbeddings()
    db = Chroma(
        persist_directory=str(persist_directory),
        collection_name=collection_name,
        embedding_function=embeddings,
    )
    return db


if __name__ == "__main__":
    print("Use retrieval/retriever.py or ingestion/run_ingestion.py to run the vector store pipeline.")
