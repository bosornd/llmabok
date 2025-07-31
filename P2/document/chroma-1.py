from unittest import result
from dotenv import load_dotenv
load_dotenv()

import ast
with open("AI 에이전트 동향_LLM_Splitted.txt", "r", encoding="utf-8") as f:
    file = f.read()
    texts = ast.literal_eval(file)

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma.from_texts(texts, embeddings, persist_directory="chroma_db")

retriever = vector_store.as_retriever()
print(retriever.invoke("ISO/IEC는 AI 에이전트를 어떻게 정의하는가?"))