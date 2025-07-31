from dotenv import load_dotenv
load_dotenv()

print("Without context ------------------------")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
response = llm.invoke("한국의 대통령은?")
print(response.content)  # Output: 현재 대한민국의 대통령은 윤석열 대통령입니다.

print("With context ---------------------------")

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
다음의 Context를 읽고, 질문에 답해줘.
Context: {context}
질문: {question}""")

chain = prompt | llm

response = chain.invoke({"question": "한국의 대통령은?",
    "context": "2025년 6월 3일에 당선된 제 21대 대통령은 더불어민주당 이재명이다."})
print(response.content)  # Output: 한국의 대통령은 이재명입니다.
