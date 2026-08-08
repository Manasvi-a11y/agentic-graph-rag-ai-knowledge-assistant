from ingestion.loader import DocumentLoader


def main():
    loader = DocumentLoader("knowledge_base")

    documents = loader.load_documents()

    print(f"Loaded {len(documents)} documents")

    if documents:
        print("\nMetadata:")
        print(documents[0].metadata)

        print("\nContent Preview:")
        print(documents[0].page_content[:500])


if __name__ == "__main__":
    main()