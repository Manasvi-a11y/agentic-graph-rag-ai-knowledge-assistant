from neo4j import GraphDatabase

from config import settings


class Neo4jManager:

    def __init__(self):

        self.driver = GraphDatabase.driver(
            settings.NEO4J_URI,
            auth=(
                settings.NEO4J_USERNAME,
                settings.NEO4J_PASSWORD,
            ),
        )

    def close(self):
        self.driver.close()

    def execute_query(
        self,
        query,
        parameters=None,
    ):

        with self.driver.session() as session:

            return session.run(
                query,
                parameters or {},
            )

    def clear_database(self):

        self.execute_query(
            "MATCH (n) DETACH DELETE n"
        )

    def create_constraint(self):

        self.execute_query(
            """
            CREATE CONSTRAINT document_name
            IF NOT EXISTS
            FOR (d:Document)
            REQUIRE d.name IS UNIQUE
            """
        )