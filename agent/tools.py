from retrieval.hybrid_retriever import HybridRetriever
from llm.generator import LLMGenerator


class AgentTools:

    def __init__(self):

        self.retriever = HybridRetriever()

        self.generator = LLMGenerator()

    def search_documents(
        self,
        query
    ):

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