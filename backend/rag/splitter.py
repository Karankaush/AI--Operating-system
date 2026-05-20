from langchain_text_splitters import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=80
)

def split_documents(documents):
    chunk = text_splitter.split_documents(documents)
    return chunk