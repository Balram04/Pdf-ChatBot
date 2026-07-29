from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()   

llm = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY"),
    temperature=0
)

prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer ONLY from the provided context.

If the answer is not in the context,
say:

"I couldn't find that information in the PDF."

Context:
{context}

Question:
{question}
""")