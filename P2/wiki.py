from dotenv import load_dotenv
load_dotenv()

from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever()

# response = retriever.invoke("한국의 대통령은?")
# print(response)

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
