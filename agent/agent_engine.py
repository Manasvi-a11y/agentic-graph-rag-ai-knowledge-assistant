from agent.router import QueryRouter
from agent.tools import AgentTools
from llm.output_parser import OutputParser


class AgentEngine:

    def __init__(self):
        self.router = QueryRouter()
        self.tools = None
        self.parser = OutputParser()

    @staticmethod
    def _build_search_query(query: str, history) -> str:
        """Combine the last couple of turns with the current query so short
        follow-ups (e.g. 'give me an example') keep the conversation's topic
        instead of searching in isolation."""
        if not history:
            return query

        recent_texts = []
        for message in history[-4:]:
            if isinstance(message, dict):
                text = message.get("text")
            else:
                text = getattr(message, "text", None)
            if text:
                recent_texts.append(text)

        recent_texts.append(query)
        return " ".join(recent_texts)

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

        search_query = self._build_search_query(query, history)

        try:
            if self.tools is None:
                self.tools = AgentTools()
            docs = self.tools.search_documents(search_query)
        except Exception as error:
            print(f"[WARNING] Document retrieval failed: {error}")
            docs = []

        if self.tools is None:
            return {
                "answer": "I couldn't find this information in the current knowledge base.",
                "sources": [],
            }

        result = self.tools.generate_response(
            query,
            docs,
            history,
        )

        return result