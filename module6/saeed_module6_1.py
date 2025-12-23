from langchain_community.document_loaders import Docx2txtLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_openai import ChatOpenAI


loader = Docx2txtLoader("data/my_document.docx")
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)
chunks = text_splitter.split_documents(documents)


embeddings = OpenAIEmbeddings(
    api_key="YOUR_API_KEY"
)

vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="./chroma_db"
)

vectorstore.persist()


retriever = vectorstore.as_retriever(
    search_kwargs={"k": 3}
)

query = "What is this document about?"

top_docs = retriever.get_relevant_documents(query)

print("\n🔍 TOP 3 RESULTS:\n")
for i, doc in enumerate(top_docs, 1):
    print(f"Result {i}:")
    print(doc.page_content)
    print("-" * 40)


llm = ChatOpenAI(
    model="gpt-4o-mini",
    api_key="YOUR_API_KEY"
)

context = "\n\n".join([doc.page_content for doc in top_docs])

prompt = f"""
Answer the question using ONLY the context below:

Context:
{context}

Question:
{query}
"""

response = llm.invoke(prompt)
print("\n LLM ANSWER:\n", response.content)

