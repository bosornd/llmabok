from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
store = {}
def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        # 세션이 없으면 ChatMessageHistory를 새로 생성합니다.
        store[session_id] = InMemoryChatMessageHistory()

    return store.get(session_id)

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 나의 친구입니다. 편안하게 대화해 주세요."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{question}"),
])

from langchain_core.runnables.history import RunnableWithMessageHistory
chain = RunnableWithMessageHistory(
    prompt | llm,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

print("대화를 시작하세요. 종료하려면 'exit'를 입력하세요.")
while True:
    question = input("You: ")
    if question.lower() == "exit": break

    response = chain.invoke({"question": question}, config={"configurable": {"session_id": "1"}})
    print("AI:", response.content)
