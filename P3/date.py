from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
오늘은 2025년 8월 1일 금요일입니다. {question}
""")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt | llm
response = chain.invoke({"question": "모레는 무슨 요일인가요?"})
print(response)