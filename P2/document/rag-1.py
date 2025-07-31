from dotenv import load_dotenv
load_dotenv()

import ast
with open("AI 에이전트 동향_LLM_Splitted.txt", "r", encoding="utf-8") as f:
    file = f.read()
    texts = ast.literal_eval(file)

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_core.vectorstores import InMemoryVectorStore
vector_store = InMemoryVectorStore(embeddings)
vector_store.add_texts(texts)

vector_store.dump("vectorstore.json")
