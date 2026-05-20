from loader import load_documents
from splitter import split_documents
from embeddings import embedding_model
from vectorstore import create_vectorstore

documents = load_documents('documents/langchain_.pdf')

chunks = split_documents(documents)
vectorstore = create_vectorstore(chunks)
print("vector DB created successfully")
