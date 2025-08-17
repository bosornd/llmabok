from langchain_core.runnables import RunnableLambda
chain = RunnableLambda(lambda x: x)

from langsmith.schemas import Run, Example

def my_score_evaluator(run: Run, example: Example) -> dict:
#   (run.outputs["result"], example.outputs["answer"])로부터 score를 계산
    import random
    return {"key": "my_score", "score": random.randint(1, 11)}   # 랜덤 평가

from langsmith.evaluation import evaluate, LangChainStringEvaluator

experiment_results = evaluate(
    lambda inputs: {"result": chain.invoke(inputs["question"])},
    data="AGENT_DATASET",
    evaluators=[my_score_evaluator],
    experiment_prefix="RAG_EVAL",
)
