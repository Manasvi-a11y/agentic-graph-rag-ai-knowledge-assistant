from pathlib import Path
from typing import List

from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
)

from langchain_core.documents import Document


class DocumentLoader:

    def __init__(self, knowledge_base: str):

        self.knowledge_base = Path(knowledge_base)

    def load_documents(self) -> List[Document]:

        documents = []

        for file in self.knowledge_base.rglob("*"):

            if file.suffix.lower() == ".pdf":

                loader = PyPDFLoader(str(file))

                documents.extend(loader.load())

            elif file.suffix.lower() in [".txt", ".md"]:

                loader = TextLoader(str(file), encoding="utf-8")

                documents.extend(loader.load())

        return documents