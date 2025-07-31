from dotenv import load_dotenv
load_dotenv()

from langchain_core.tools import tool
from datetime import datetime
@tool
def get_today():
  """오늘의 날짜와 요일을 반환합니다."""
  return datetime.today().strftime("%Y년 %m월 %d일 %A")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")
llm_with_tools = llm.bind_tools([get_today])    # Bind tools to LLM

from langchain_core.messages import SystemMessage, HumanMessage
messages = [SystemMessage(content="당신은 도구를 사용하는 AI입니다."),
            HumanMessage(content="모레는 무슨 요일인가요?")]

ai_message = llm_with_tools.invoke(messages)

if hasattr(ai_message, "tool_calls") and ai_message.tool_calls:
    messages.append(ai_message)

    for tool_call in ai_message.tool_calls:
        if tool_call["name"] == "get_today":
            messages.append(get_today.invoke(tool_call))

    ai_message = llm_with_tools.invoke(messages)
    print(ai_message)
