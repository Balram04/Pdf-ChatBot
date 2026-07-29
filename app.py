from langchain_community.document_loaders import PyPDFLoader
from utils.splitter import get_text_splitter
from utils.embeddings import get_embedding_model
from utils.vectorstore import create_vector_store
from utils.retriever import get_retriever
from utils.chain import create_rag_chain



loader = PyPDFLoader("data/resume.pdf")
documents = loader.load()

splitter = get_text_splitter()
chunks = splitter.split_documents(documents)

embedding_model = get_embedding_model()

vector_store = create_vector_store(chunks, embedding_model)

retriever = get_retriever(vector_store)

rag_chain = create_rag_chain(retriever)

while True:

    question = input("\nAsk: ")

    if question.lower() == "exit":
        break

    answer = rag_chain.invoke(question)

    print("\nAnswer:\n")
    print(answer)