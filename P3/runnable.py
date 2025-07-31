from langchain_core.runnables import RunnableLambda

runnable = RunnableLambda(lambda x: x["a"] + x["b"])
print(runnable.invoke({"a": 2, "b": 3}))  # 5

tool = runnable.as_tool(name="add", description="Add two numbers.")
print(tool.name)         # add
print(tool.description)  # Add two numbers.
print(tool.args)         # {'a': {'title': 'A'}, 'b': {'title': 'B'}}

from pydantic import BaseModel, Field
class CalculatorInput(BaseModel):
    a: int = Field(description="the left operand.")
    b: int = Field(description="the right operand.")

tool = runnable.as_tool(name="add", description="Add two numbers.", args_schema=CalculatorInput)
print(tool.name)         # add
print(tool.description)  # Add two numbers.
print(tool.args)         # {'a': {'description': 'the left operand.', 'title': 'A', 'type': 'integer'}, 'b': {'description': 'the right operand.', 'title': 'B', 'type': 'integer'}}
