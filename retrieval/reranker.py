class ReRanker:

    def rerank(
        self,
        vector_results,
        graph_results
    ):

        combined = []

        combined.extend(vector_results)

        combined.extend(graph_results)

        return combined