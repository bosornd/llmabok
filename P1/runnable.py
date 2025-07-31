from langchain_core.runnables import RunnableLambda

r1 = RunnableLambda(lambda x: x + 1)
r2 = RunnableLambda(lambda x: x * 2)
r3 = RunnableLambda(lambda x: x * 5)

result = r1.invoke(1)
print(result)  # 2

result = r1.batch([1, 2, 3])
print(result)  # [2, 3, 4]

from langchain_core.runnables import RunnableSequence
chain = RunnableSequence(r1, r2)        # r1 | r2
result = chain.invoke(1)
print(result)  # 4

from langchain_core.runnables import RunnableParallel
chain = RunnableParallel(mul_2=r2, mul_5=r3)  # {'mul_2': r2, 'mul_5': r3}
result = chain.invoke(2)
print(result)  # {'mul_2': 4, 'mul_5': 10}

chain = r1 | {'mul_2': r2, 'mul_5': r3}
result = chain.invoke(1)
print(result)  # {'mul_2': 4, 'mul_5': 10}

from langchain_core.runnables import RunnableBranch
branch = RunnableBranch(
    (lambda x: x < 0, lambda x: -x),
    (lambda x: x < 10, lambda x: x + 10),
    lambda x: x
)

print(branch.invoke(-5))  # 5
print(branch.invoke(5))   # 15
print(branch.invoke(25))  # 25