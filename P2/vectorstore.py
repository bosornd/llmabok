import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# pip install sentence-transformers
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)

texts = [
    "삼성 가우스는 삼성전자의 멀티모달 모델의 생성형 인공지능이다.",
    "2025년 당선된 대한민국의 대통령은 더불어민주당 이재명이다.",
]
vector_store.add_texts(texts)
print(vector_store.similarity_search("한국의 대통령은?", 1))

retriever = vector_store.as_retriever()

#################### general rag chain ####################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음 context를 근거로 질문에 답하세요.\ncontext: {context}\n질문: {question}\n")

from langchain_core.runnables import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
#################### general rag chain ####################

response = chain.invoke("한국의 대통령은?")
print(response.content)
