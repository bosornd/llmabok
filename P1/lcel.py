from langchain_core.runnables import RunnableLambda, RunnableSequence, RunnableParallel, RunnableBranch

r = RunnableLambda(lambda x: x + 1)
result = r.invoke(1)
print(result)           # 2

result = r.batch([1, 2, 3])
print(result)           # [2, 3, 4]

r2 = RunnableLambda(lambda x: x * 2)
r3 = RunnableLambda(lambda x: x * 5)

seq = RunnableSequence(r, r2, r3)
result = seq.invoke(1)
print(result)           # 20

p = RunnableParallel({"mul_2": r2, "mul_5": r3})
result = p.invoke(2)
print(result)           # {'mul_2': 4, 'mul_5': 10}

chain = r | {"mul_2": r2, "mul_5": r3}
result = chain.invoke(1)
print(result)           # {'mul_2': 4, 'mul_5': 10}

b = RunnableBranch(
    (lambda x: x < 0, lambda x: -x),
    (lambda x: x)
)
print(b.invoke(-5))  # 5
print(b.invoke(5))   # 5