from retrieval.hybrid_retriever import HybridRetriever
from llm.generator import LLMGenerator


class AgentTools:

    def __init__(self):
        self.generator = LLMGenerator()

        try:
            self.retriever = HybridRetriever()
        except Exception as error:
            print(f"[WARNING] Retriever initialization failed: {error}")
            self.retriever = None

    def search_documents(
        self,
        query
    ):
        if self.retriever is None:
            raise RuntimeError("Document retrieval is unavailable")
        return self.retriever.retrieve(query)

    def generate_response(
        self,
        query,
        docs,
        history=None
    ):

        return self.generator.generate(
            query,
            docs,
            history,
        )