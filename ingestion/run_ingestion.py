from ingestion.loader import DocumentLoader
from ingestion.splitter import DocumentSplitter
from ingestion.vector_indexer import VectorIndexer
from ingestion.graph_indexer import GraphIndexer


def main():
    loader = DocumentLoader("knowledge_base")
    documents = loader.load_documents()

    splitter = DocumentSplitter()
    chunks = splitter.split_documents(documents)

    vector_db = VectorIndexer()
    vector_db.create_vector_store(chunks)

    graph_db = GraphIndexer()
    graph_db.build_graph(chunks)

    print("\nIngestion Completed Successfully")


if __name__ == "__main__":
    main()