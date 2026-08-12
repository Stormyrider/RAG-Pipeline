from loader import load_document
from chunker import chunk_documents
from vector_store import add_documents, search


documents = load_document("data/documents/rag_notes.md")
chunks = chunk_documents(documents)

add_documents(chunks)

results = search("What is RAG?", 3)

for result in results:
    print("\n--- Result ---")
    print(result.page_content)
    print(result.metadata)