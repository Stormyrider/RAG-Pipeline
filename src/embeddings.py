from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import os

load_dotenv()


def create_embeddings():
    return OpenAIEmbeddings(
        model="openai/text-embedding-3-small",
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )