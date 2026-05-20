import os
from langchain_core.prompts import ChatPromptTemplate
from vectorstore import load_vectorstore
from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()


api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(
    api_key=api_key,
    model="llama-3.1-8b-instant",
    temperature=0.7,
)

vectorstore = load_vectorstore()

retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

prompt = ChatPromptTemplate.from_template(
    """
    You are a helpful assistant that provides information based on the retrieved documents.
    Use the following retrieved documents to answer the question.
    
   Context:
    {context}

    Question:
    {question}
    """
)



while True:
    question = input("Enter your question (or 'exit' to quit): ")
    if question.lower() == 'exit':
        break
    results = retriever.invoke(question)
    context = "\n\n".join([doc.page_content for doc in results])

    chain = prompt | model
    response = chain.invoke({"context": context, "question": question})
    print(response.content)