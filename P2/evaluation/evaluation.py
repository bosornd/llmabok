from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="../document/chroma_db")
retriever = vector_store.as_retriever()

#################### general rag chain ####################
from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("다음 context를 근거로 질문에 답하세요.\ncontext: {context}\n질문: {question}\n")

from langchain_core.runnables import RunnablePassthrough
chain = { "context": retriever, "question": RunnablePassthrough() } | prompt | llm
#################### general rag chain ####################

from langsmith.evaluation import evaluate, LangChainStringEvaluator

from langsmith.evaluation import LangChainStringEvaluator
qa_evalulator = LangChainStringEvaluator("qa", config={"llm": llm})
# qa_evalulator.evaluator.prompt.pretty_print()

conciseness_evalulator = LangChainStringEvaluator("criteria",
                             config={"criteria": "conciseness", "llm": llm})
conciseness_evalulator.evaluator.prompt.pretty_print()

relevance_evalulator = LangChainStringEvaluator("criteria",
                             config={"criteria": "relevance", "llm": llm})

correctness_evalulator = LangChainStringEvaluator("labeled_criteria",
                             config={"criteria": "correctness", "llm": llm},
                             prepare_data=lambda run, example: {
                              "prediction": run.outputs["result"],
                              "reference": example.outputs["answer"],
                              "input": example.inputs["question"],
                             })

embedding_evaluator = LangChainStringEvaluator(
    "embedding_distance",
    config={
        "embeddings": embeddings,
        "distance_metric": "cosine",
    },
)

experiment_results = evaluate(
    lambda inputs: {"result": chain.invoke(inputs["question"])},
    data="AGENT_DATASET",
    evaluators=[qa_evalulator, conciseness_evalulator, relevance_evalulator, correctness_evalulator, embedding_evaluator],
    experiment_prefix="RAG_EVAL",
)
