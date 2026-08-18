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

        files = list(self.knowledge_base.rglob("*"))

        print(f"Found {len(files)} files in knowledge base\n")

        for file in files:

            # ==========================
            # PDF FILES
            # ==========================

            if file.suffix.lower() == ".pdf":

                try:
                    loader = PyPDFLoader(str(file))

                    loaded_docs = loader.load()

                    documents.extend(loaded_docs)

                    print(
                        f"OK     : {file} "
                        f"({len(loaded_docs)} pages)"
                    )

                except Exception as e:

                    print(f"ERROR  : {file}")
                    print(f"         {e}")
                    print("         Skipping this PDF...\n")

                    continue

            # ==========================
            # TEXT / MARKDOWN FILES
            # ==========================

            elif file.suffix.lower() in [".txt", ".md"]:

                try:
                    loader = TextLoader(
                        str(file),
                        encoding="utf-8"
                    )

                    loaded_docs = loader.load()

                    documents.extend(loaded_docs)

                    print(f"OK     : {file}")

                except Exception as e:

                    print(f"ERROR  : {file}")
                    print(f"         {e}")
                    print("         Skipping this file...\n")

                    continue

        print("\n==============================")
        print(f"Total documents loaded: {len(documents)}")
        print("==============================\n")

        return documents