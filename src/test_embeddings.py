from embeddings import create_embeddings

embeddings = create_embeddings()

vector = embeddings.embed_query("Python is a programming language.")

print("Embedding created successfully")
print("Vector length:", len(vector))