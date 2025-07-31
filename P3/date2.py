from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("오늘은 {today}입니다. {question}")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt | llm

from datetime import datetime
today = datetime.now().strftime("%Y년 %m월 %d일 %A")

response = chain.invoke({"today": today, "question": "모레는 무슨 요일인가요?"})
print(response)