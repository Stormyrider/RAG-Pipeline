from dotenv import load_dotenv
import os

load_dotenv()

if os.getenv("OPENROUTER_API_KEY"):
    print("OpenRouter API key loaded successfully")
else:
    print("OpenRouter API key not found")