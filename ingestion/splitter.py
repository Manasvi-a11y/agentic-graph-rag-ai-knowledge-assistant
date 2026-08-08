from typing import List

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import settings


class DocumentSplitter:
    """
    Splits loaded documents into smaller chunks for retrieval.
    """

    def __init__(self):
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                "? ",
                "! ",
                " ",
                ""
            ]
        )

    def split_documents(
        self,
        documents: List[Document]
    ) -> List[Document]:

        chunks = self.splitter.split_documents(documents)

        for idx, chunk in enumerate(chunks):
            chunk.metadata["chunk_id"] = idx

        print(f"Created {len(chunks)} chunks.")

        return chunks