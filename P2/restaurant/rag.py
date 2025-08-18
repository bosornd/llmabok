from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="chroma_db")

from langchain_community.cross_encoders import HuggingFaceCrossEncoder
cross_encoder = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-v2-m3")

from langchain.retrievers.document_compressors import CrossEncoderReranker
reranker = CrossEncoderReranker(model=cross_encoder)

from langchain.retrievers import ContextualCompressionRetriever
retriever = ContextualCompressionRetriever(
    base_compressor=reranker, base_retriever=vector_store.as_retriever()
)

#################### general rag chain ####################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음 context를 근거로 질문에 답하세요.\ncontext: {context}\n질문: {question}\n")

from langchain_core.runnables import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
#################### general rag chain ####################

response = chain.invoke("주차와 흡연이 가능한 맛집은?")
print(response.content)