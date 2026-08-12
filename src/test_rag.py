from loader import load_document
from chunker import chunk_documents
from vector_store import add_documents
from rag_pipeline import ask


documents = load_document("data/documents/technova_knowledge.md")
chunks = chunk_documents(documents)

add_documents(chunks)

question = "Who is the president of Pakistan?"

answer, sources = ask(question)

print("\nAnswer:")
print(answer)

print("\nSources:")
for source in sources:
    print("-", source)