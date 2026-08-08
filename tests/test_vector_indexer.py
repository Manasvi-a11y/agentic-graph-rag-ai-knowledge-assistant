from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from ingestion.vector_indexer import VectorIndexer

loader = DocumentLoader("knowledge_base")
documents = loader.load_documents()

splitter = DocumentSplitter()
chunks = splitter.split_documents(documents)

db = VectorIndexer()

db.create_vector_store(chunks)