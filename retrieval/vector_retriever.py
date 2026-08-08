from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings


class VectorRetriever:

    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )

        self.db = Chroma(
            persist_directory="./vector_db/chroma",
            embedding_function=self.embeddings
        )

    def retrieve(self, query, k=5):

        docs = self.db.similarity_search(query, k=k)

        print("\n==========================")
        print("QUERY:", query)
        print("Retrieved:", len(docs))

        for i, doc in enumerate(docs):
            print(f"\nDocument {i+1}")
            print(doc.metadata)
            print(doc.page_content[:300])

        print("==========================\n")

        return docs