import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("오늘은 {today}입니다. {question}")

from datetime import datetime
from langchain_core.runnables import RunnablePassthrough
chain = { "today": lambda x: datetime.today().strftime("%Y년 %m월 %d일 %A"),
          "question": RunnablePassthrough() } | prompt | llm

response = chain.invoke({"question": "모레는 무슨 요일인가요?"})
print(response.content)