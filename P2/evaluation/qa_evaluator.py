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

from langsmith.evaluation import LangChainStringEvaluator
qa_evalulator = LangChainStringEvaluator("qa", config={"llm": llm})
qa_evalulator.evaluator.prompt.pretty_print()

embedding_evaluator = LangChainStringEvaluator(
    "embedding_distance",
    config={
        "embeddings": embeddings,
        "distance_metric": "cosine",
    },
)

from langsmith.evaluation import evaluate
experiment_results = evaluate(
    lambda inputs: {"result": chain.invoke(inputs["question"])},
    data="AGENT_DATASET",
    evaluators=[qa_evalulator, embedding_evaluator],
    experiment_prefix="RAG_EVAL",
)
