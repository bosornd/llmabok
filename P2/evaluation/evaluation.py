from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="../document/chroma_db")
retriever = vector_store.as_retriever()

################################################# RAG #################################################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
다음의 Context를 읽고, 질문에 답해줘.
Context: {context}
질문: {question}""")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain.schema.runnable import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm | StrOutputParser()
################################################# RAG #################################################

from langsmith.schemas import Run, Example
def my_score_evaluator(run: Run, example: Example) -> dict:
#   (run.outputs["result"], example.outputs["answer"])로부터 score를 계산
    import random
    return {"key": "my_score", "score": random.randint(1, 11)}  # 랜덤 평가

from langsmith.evaluation import evaluate
experiment_results = evaluate(
    lambda inputs: {"result": chain.invoke(inputs["question"])},
    data="AGENT_DATASET",
    evaluators=[my_score_evaluator],
    experiment_prefix="RAG_EVAL",
)
