from vectorstore import load_vectorstore
vectorstore = load_vectorstore()

retriever = vectorstore.as_retriever(
    search_kwargs={"k" : 3}
)

query = input("Enter your query")

results = retriever.invoke(query)

for i, doc in enumerate(results):
    print(f"Result {i+1}")
    print(doc.page_content)

