from pathlib import Path
from typing import List

from langchain.document_loaders import PyPDFLoader
from langchain.schema import Document


def list_pdf_paths(root_dir: Path) -> List[Path]:
    return sorted(root_dir.rglob("*.pdf"))


def load_documents(root_dir: Path) -> List[Document]:
    root_dir = Path(root_dir)
    documents: List[Document] = []

    for pdf_path in list_pdf_paths(root_dir):
        loader = PyPDFLoader(str(pdf_path))
        pdf_docs = loader.load()
        for doc in pdf_docs:
            metadata = dict(doc.metadata)
            metadata["source_file"] = str(pdf_path.relative_to(root_dir))
            metadata["source_path"] = str(pdf_path)
            documents.append(Document(page_content=doc.page_content, metadata=metadata))

    return documents


if __name__ == "__main__":
    root = Path(__file__).resolve().parent.parent / "knowledge_base"
    docs = load_documents(root)
    print(f"Loaded {len(docs)} document chunks from {root}")
