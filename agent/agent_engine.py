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
        """Add only the immediately preceding USER question (never the long
        assistant answers) so short follow-ups keep context, without
        drowning fresh, self-contained questions in unrelated terminology."""
        if not history:
            return query

        previous_user_text = None
        for message in reversed(history):
            if isinstance(message, dict):
                sender = message.get("sender")
                text = message.get("text")
            else:
                sender = getattr(message, "sender", None)
                text = getattr(message, "text", None)

            if sender == "user" and text and text.strip() != query.strip():
                previous_user_text = text
                break

        if not previous_user_text:
            return query

        return f"{previous_user_text} {query}"

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