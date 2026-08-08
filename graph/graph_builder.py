from graph.neo4j_manager import Neo4jManager
from graph.entity_extractor import EntityExtractor
from graph.cypher_queries import (
    CREATE_DOCUMENT,
    CREATE_ENTITY,
    LINK_ENTITY,
)


class GraphBuilder:

    def __init__(self):

        self.neo4j = Neo4jManager()

        self.extractor = EntityExtractor()

    def create_graph(self, chunks):

        for chunk in chunks:

            filename = chunk.metadata["filename"]

            category = chunk.metadata["category"]

            self.neo4j.execute_query(
                CREATE_DOCUMENT,
                {
                    "name": filename,
                    "category": category,
                },
            )

            entities = self.extractor.extract_entities(
                chunk.page_content
            )

            for entity in entities:

                self.neo4j.execute_query(
                    CREATE_ENTITY,
                    {
                        "entity": entity["text"],
                    },
                )

                self.neo4j.execute_query(
                    LINK_ENTITY,
                    {
                        "document": filename,
                        "entity": entity["text"],
                    },
                )

        print("Knowledge Graph Built Successfully")