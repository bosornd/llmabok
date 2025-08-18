import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

class SimpleRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str) -> list[Document]:
        return [Document(page_content="2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다.")]

retriever = SimpleRetriever()

#################### general rag chain ####################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음 context를 근거로 질문에 답하세요.\ncontext: {context}\n질문: {question}\n")

from langchain_core.runnables import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
#################### general rag chain ####################

response = chain.invoke("한국의 대통령은?")
print(response.content)

