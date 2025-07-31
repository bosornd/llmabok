from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 나의 친구입니다. 편안하게 대화해 주세요."),
    MessagesPlaceholder(variable_name="history"),
])

chain = prompt | llm

print("대화를 시작하세요. 종료하려면 'exit'를 입력하세요.")
history = []
while True:
    question = input("You: ")
    if question.lower() == "exit": break
    history.append(("human", question))

    response = chain.invoke({"history": history})
    print("AI:", response.content)
    history.append(("ai", response.content))
