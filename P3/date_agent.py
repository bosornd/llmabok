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

from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
prompt = ChatPromptTemplate.from_messages([
    ("system", "당신은 도구를 사용하는 AI입니다."),
    ("user", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

from langchain.agents import create_tool_calling_agent, AgentExecutor
agent = create_tool_calling_agent(llm, [get_today], prompt)
agent_executor = AgentExecutor(agent=agent, tools=[get_today])

response = agent_executor.invoke({"input": "모레는 무슨 요일인가요?"})
print(response)
