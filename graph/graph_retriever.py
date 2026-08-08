from graph.neo4j_manager import Neo4jManager


class GraphRetriever:

    def __init__(self):

        self.neo4j = Neo4jManager()

    def search(self, entity):

        query = """
        MATCH (d)-[:CONTAINS]->(e)

        WHERE toLower(e.name)=toLower($entity)

        RETURN d.name,d.category
        """

        result = self.neo4j.execute_query(
            query,
            {"entity": entity},
        )

        return [record.data() for record in result]