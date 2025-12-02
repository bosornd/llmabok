import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

from langchain_core.documents import Document
from langchain_core.retrievers import BaseRetriever

class SimpleRetriever(BaseRetriever):
    def _get_relevant_documents(self, query: str) -> list[Document]:
        return [Document(page_content="2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다.")]

retriever = SimpleRetriever()

context = retriever.invoke("한국의 대통령은?")
print(context)

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
        다음 context를 근거로 질문에 답하세요.
        context: {context}
        question: {question}
        """)

chain = prompt | llm
chain.invoke({
    "context": retriever.invoke("한국의 대통령은?"),
    "question": "한국의 대통령은?"
})
