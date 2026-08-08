from graph.graph_builder import GraphBuilder


class GraphIndexer:

    def __init__(self):

        self.builder = GraphBuilder()

    def build_graph(self, chunks):

        self.builder.create_graph(chunks)

        print("Knowledge Graph Created")