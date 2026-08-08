from graph.entity_extractor import EntityExtractor

extractor = EntityExtractor()

text = """
LangChain uses ChromaDB for Vector Search.

Neo4j stores Knowledge Graph.

OpenAI developed GPT.
"""

entities = extractor.extract_entities(text)

for entity in entities:
    print(entity)