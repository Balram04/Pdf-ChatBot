from dotenv import load_dotenv
import os
from pathlib import Path
from langchain_google_genai import GoogleGenerativeAIEmbeddings

# Load .env from the project root (two levels up from this file)
project_root = Path(__file__).resolve().parents[1]
load_dotenv(dotenv_path=project_root / ".env")

def get_embedding_model():
    api_key = os.getenv("GOOGLE_API_KEY")

    if not api_key:
        raise RuntimeError(
            "Missing Google API key. Set GOOGLE_API_KEY in your .env file."
        )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="gemini-embedding-001",
        google_api_key=api_key
    )

    return embeddings