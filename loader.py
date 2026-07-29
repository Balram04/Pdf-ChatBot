from langchain_community.document_loaders import PyPDFLoader
from utils.embeddings import get_embedding_model
from utils.splitter import get_text_splitter
from utils.vectorstore import create_vector_store
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

loader = PyPDFLoader("data/resume.pdf")
documents = loader.load()

splitter = get_text_splitter()
chunks = splitter.split_documents(documents)

embedding_model = get_embedding_model()

vector = embedding_model.embed_query(chunks[0].page_content)

vector_store = create_vector_store(
    chunks,
    embedding_model
)

print("Vector Store Created Successfully")

print(splitter)
print(chunks[5].page_content)
print(type(vector))
print(len(vector))
print(vector[:10])
from langchain_community.document_loaders import PyPDFLoader



