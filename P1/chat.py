import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 나의 친구입니다. 편안하게 대화해 주세요."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}")
])

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
chain = prompt | llm

print("대화를 시작하세요. 종료하려면 'exit'를 입력하세요.")
history = []
while True:
    question = input("You: ")
    if question.lower() == "exit": break

    response = chain.invoke({"history": history, "question": question})
    print("AI:", response.content)

    history.append(("human", question))
    history.append(("ai", response.content))