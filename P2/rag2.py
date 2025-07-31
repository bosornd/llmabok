from dotenv import load_dotenv
load_dotenv()

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever
class SimpleRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str) -> list[Document]:
        return [Document(page_content="2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다.")]

retriever = SimpleRetriever()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
다음의 Context를 읽고, 질문에 답해줘.
Context: {context}
질문: {question}""")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt | llm

question = "한국의 대통령은?"
response = chain.invoke({"context": retriever.invoke(question), "question": question})
print(response.content)
