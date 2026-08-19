from agent.router import QueryRouter
from agent.tools import AgentTools
from llm.output_parser import OutputParser


class AgentEngine:

    def __init__(self):
        self.router = QueryRouter()
        self.tools = None
        self.parser = OutputParser()

    def chat(self, query: str, history: list[dict] | None = None):

        route = self.router.route(query)

        if route == "greeting":
            return {
                "answer": (
                    "Hello 👋\n\n"
                    "I am your AI & Computer Science Knowledge Assistant.\n"
                    "Ask me anything related to AI, ML, DL, Python, Java, DSA, SQL, AWS, RAG, LangChain, or Graph RAG."
                ),
                "sources": []
            }

        try:
            if self.tools is None:
                self.tools = AgentTools()
            docs = self.tools.search_documents(query)
        except Exception as error:
            print(f"[WARNING] Document retrieval failed: {error}")
            docs = []

        result = self.tools.generate_response(
            query,
            docs,
            history,
        )

        return result