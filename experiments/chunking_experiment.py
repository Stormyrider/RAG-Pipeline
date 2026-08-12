import sys
sys.path.append("src")

from loader import load_document
from langchain_text_splitters import RecursiveCharacterTextSplitter


documents = load_document("data/documents/rag_notes.md")

settings = [
    (300, 30),
    (500, 50),
    (800, 80)
]

for chunk_size, overlap in settings:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=overlap
    )

    chunks = splitter.split_documents(documents)

    print(f"Chunk size: {chunk_size}")
    print(f"Overlap: {overlap}")
    print(f"Number of chunks: {len(chunks)}")
    print("-" * 30)