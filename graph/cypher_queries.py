CREATE_DOCUMENT = """
MERGE (d:Document {name:$name})
SET d.category=$category
"""

CREATE_ENTITY = """
MERGE (e:Entity {name:$entity})
"""

LINK_ENTITY = """
MATCH (d:Document {name:$document})

MATCH (e:Entity {name:$entity})

MERGE (d)-[:CONTAINS]->(e)
"""