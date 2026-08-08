from ingestion.embedding import EmbeddingModel

embedding = EmbeddingModel()

model = embedding.get_embedding_model()

vector = model.embed_query("What is Artificial Intelligence?")

print(len(vector))