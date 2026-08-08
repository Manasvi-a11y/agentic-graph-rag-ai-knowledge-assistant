from graph.neo4j_manager import Neo4jManager


class GraphRetriever:

    def __init__(self):
        self.neo4j = Neo4jManager()

    def retrieve(self, entity):

        query = """
        MATCH (d)-[:CONTAINS]->(e)
        WHERE toLower(e.name)=toLower($entity)
        RETURN d.name,d.category
        """

        try:
            result = self.neo4j.execute_query(
                query,
                {"entity": entity}
            )

            return [
                record.data()
                for record in result
            ]
        except Exception as error:
            print(f"[WARNING] Neo4j query failed for entity '{entity}': {error}")
            return []
