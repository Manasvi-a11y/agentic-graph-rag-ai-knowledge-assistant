from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter


loader = DocumentLoader("knowledge_base")
documents = loader.load_documents()

splitter = DocumentSplitter()

chunks = splitter.split_documents(documents)

print(len(chunks))

print(chunks[0].metadata)

print(chunks[0].page_content)