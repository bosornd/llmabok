import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_core.tools import tool
from datetime import datetime

@tool
def get_today() -> str:
    """오늘의 날짜와 요일을 반환합니다."""
    return datetime.today().strftime("%Y년 %m월 %d일 %A")

llm_with_tools = llm.bind_tools([get_today])

from langchain_core.messages import SystemMessage, HumanMessage, ToolMessage
messages = [SystemMessage(content="오늘의 날짜와 요일은 'get_today' 함수로 확인하세요."),
            HumanMessage(content="모레는 무슨 요일인가요?")]

ai_message = llm_with_tools.invoke(messages)
print(ai_message)
messages.append(ai_message)

for tool_call in ai_message.tool_calls:
    if tool_call["name"] == "get_today":
        messages.append(ToolMessage(content=get_today.invoke({}),
                                    tool_call_id=tool_call["id"]))

ai_message = llm_with_tools.invoke(messages)
print(ai_message)