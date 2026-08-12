from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from vector_store import search
from dotenv import load_dotenv
import os


load_dotenv()

llm = ChatOpenAI(
    model="openrouter/free",
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)


prompt = ChatPromptTemplate.from_template("""
You are a restricted knowledge-base assistant.

Answer the question using only the information in the provided context.

Do not use outside knowledge or make assumptions.

If the answer is not contained in the context, say:
"The information is not available in the provided knowledge base."

Context:
{context}

Question:
{question}
""")

def retrieve_context(question):
    documents = search(question, 3)

    context = "\n\n".join(
        document.page_content for document in documents
    )

    return context, documents


def generate_answer(question):
    context, documents = retrieve_context(question)

    messages = prompt.format_messages(
        context=context,
        question=question
    )

    answer = llm.invoke(messages)

    return answer.content, documents


def get_sources(documents):
    sources = []

    for document in documents:
        source = document.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

    return sources


def ask(question):
    answer, documents = generate_answer(question)
    sources = get_sources(documents)

    return answer, sources