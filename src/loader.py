from langchain_community.document_loaders import PyPDFLoader, TextLoader


def load_document(path):
    if path.endswith(".pdf"):
        loader = PyPDFLoader(path)
    elif path.endswith(".md") or path.endswith(".txt"):
        loader = TextLoader(path)
    else:
        raise ValueError("Unsupported file type")

    return loader.load()