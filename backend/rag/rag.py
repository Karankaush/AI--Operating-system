from rag.loader import load_documents

from rag.splitter import split_documents

from rag.vectorstore import create_vectorstore


def ingest_pdf(file_path: str):

    documents = load_documents(
        file_path
    )

    chunks = split_documents(
        documents
    )

    create_vectorstore(chunks)

    print("PDF ingested successfully")