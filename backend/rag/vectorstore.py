from langchain_chroma import Chroma

from .embeddings import embedding_model

def create_vectorstore(chunks):
    vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="chroma_db"
    )
    return vectorstore

def load_vectorstore():
    vectorstore = Chroma(
        persist_directory="chroma_db",
        embedding_function=embedding_model
    )
    return vectorstore