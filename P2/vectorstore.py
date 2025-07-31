from dotenv import load_dotenv
load_dotenv()

# pip install sentence-transformers
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)

from langchain_core.documents import Document
docs = [
    Document(page_content="삼성 가우스는 삼성전자의 멀티모달 모델의 생성형 인공지능이다."),
    Document(page_content="2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다."),
]
vector_store.add_documents(docs)
retriever = vector_store.as_retriever(
    search_kwargs={"k": 1}  # Retrieve the most relevant document
)

# print(retriever.invoke("한국의 대통령은?"))

####################################### RAG #######################################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
다음의 Context를 읽고, 질문에 답해줘.
Context: {context}
질문: {question}""")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain.schema.runnable import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
####################################### RAG #######################################

response = chain.invoke("한국의 대통령은?")
print(response.content)
