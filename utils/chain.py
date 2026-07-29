from dotenv import load_dotenv
import os

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()


def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def create_rag_chain(retriever):

    llm = ChatGoogleGenerativeAI(
        model="gemini-3.5-flash",
        google_api_key=os.getenv("GOOGLE_API_KEY"),
        temperature=0
    )

    prompt = ChatPromptTemplate.from_template("""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not present in the context,
reply exactly:
"I am sorry, but I cannot provide an answer based on the given context."
Context:
{context}

Question:
{question}
""")

    parser = StrOutputParser()

    rag_chain = (
        {
            "context": retriever | format_docs,
            "question": RunnablePassthrough(),
        }
        | prompt
        | llm
        | parser
    )

    return rag_chain