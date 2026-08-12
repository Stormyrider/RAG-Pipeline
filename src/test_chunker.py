from loader import load_document
from chunker import chunk_documents

documents = load_document("data/documents/python.md")
chunks = chunk_documents(documents)

print("Number of chunks:", len(chunks))

for i, chunk in enumerate(chunks):
    print(f"\nChunk {i + 1}:")
    print(chunk.page_content)
    print(chunk.metadata)