from langchain_text_splitters import RecursiveCharacterTextSplitter

def get_text_splitter():
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=20
    )
    return splitter