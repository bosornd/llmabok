from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_experimental.tools import PythonREPLTool

python_tool = PythonREPLTool()
# print(python_tool.invoke("print(100 + 200)"))     # 300

def print_and_execute(code: str) -> str:
    print(f"Received code:\n{code}\n")
    # Remove Markdown code block markers if present
    if code.strip().startswith("```") and code.strip().endswith("```"):
        code = "\n".join(code.strip().splitlines()[1:-1])

    print(f"Executing code:\n{code}\n")
    return python_tool.invoke(code)

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("""
You are an expert Python programmer. Your task is to help me write Python code.
Code should be runnable in a Python REPL environment. Don't use if __name__ == "__main__":.
Return only the code, NO explanation, NO code blocks. Don't use Markdown code block markers.
---
Here is the requirement: {input}
""")

from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
# chain = prompt | llm | StrOutputParser() | python_tool
chain = prompt | llm | StrOutputParser() | RunnableLambda(print_and_execute)

response = chain.invoke("다이아몬드 모양을 출력하는 코드를 작성해줘. 입력 n은 5로.")
print(f"Result:\n{response}\n")