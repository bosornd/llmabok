import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

# pip install wikipedia
from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever()

#################### general rag chain ####################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음 context를 근거로 질문에 답하세요.\ncontext: {context}\n질문: {question}\n")

from langchain_core.runnables import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
#################### general rag chain ####################

response = chain.invoke("한국의 대통령은?")
print(response.content)
