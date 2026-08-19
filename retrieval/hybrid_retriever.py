from retrieval.vector_retriever import VectorRetriever
from retrieval.graph_retriever import GraphRetriever
from graph.entity_extractor import EntityExtractor


class HybridRetriever:

    def __init__(self):
        self.vector = VectorRetriever()
        self.graph = None
        self.extractor = None

        try:
            self.graph = GraphRetriever()
            self.extractor = EntityExtractor()
        except Exception as error:
            print(f"[WARNING] Graph retrieval disabled: {error}")

    def retrieve(self, query):

        # Retrieve from Vector DB
        vector_docs = self.vector.retrieve(query)

        # Retrieve from Graph DB
        graph_docs = []

        if self.graph is not None and self.extractor is not None:
            entities = self.extractor.extract_entities(query)

            for entity in entities:
                graph_docs.extend(
                    self.graph.retrieve(entity["text"])
                )

        # Merge both results
        combined_docs = []

        combined_docs.extend(vector_docs)
        combined_docs.extend(graph_docs)

        print("\n========== Hybrid Retrieval ==========")
        print("Vector Docs :", len(vector_docs))
        print("Graph Docs  :", len(graph_docs))
        print("Total Docs  :", len(combined_docs))
        print("======================================\n")

        return combined_docs