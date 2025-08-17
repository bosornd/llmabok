from langchain_core.runnables import RunnableLambda

r = RunnableLambda(lambda x: x + 1)
result = r.invoke(1)
print(result)           # 2

result = r.batch([1, 2, 3])
print(result)           # [2, 3, 4]
