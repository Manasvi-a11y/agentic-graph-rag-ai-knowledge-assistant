class QueryRouter:
    """
    Routes user queries.
    """

    def __init__(self):
        pass

    def route(self, query: str):

        query = query.lower()

        greetings = [
            "hi",
            "hello",
            "hey",
            "good morning",
            "good evening",
        ]

        if query in greetings:
            return "greeting"

        return "knowledge"