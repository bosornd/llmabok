from langchain_core.tools import tool

from langchain_core.runnables import RunnableLambda
runnable = RunnableLambda(lambda x: x["a"] + x["b"])
print(runnable.invoke({"a": 2, "b": 3}))

add = runnable.as_tool(name="add", description="Add two numbers.", arg_types={"a": int, "b": int})

print(type(add))
print(add.name)
print(add.description)
print(add.args)

print(add.invoke({"a": 2, "b": 3}))         # 5
