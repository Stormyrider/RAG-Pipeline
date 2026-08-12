from langchain_chroma import Chroma
from embeddings import create_embeddings


embeddings = create_embeddings()

vector_store = Chroma(
    collection_name="documents",
    persist_directory="data/chroma",
    embedding_function=embeddings
)


def add_documents(documents):
    vector_store.add_documents(documents)


def search(query, k=3):
    return vector_store.similarity_search(query, k=k)