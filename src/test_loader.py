from loader import load_document

documents = load_document("data/documents/python.md")

for document in documents:
    print(document.page_content)
    print(document.metadata)