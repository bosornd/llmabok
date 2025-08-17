from langchain_experimental.tools import PythonREPLTool

tool = PythonREPLTool()
response = tool.invoke("print(100 + 200)")
print(response)
