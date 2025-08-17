# pip install pandas
import pandas as pd     # Importing pandas for data manipulation

df = pd.read_csv("restaurant_reviews_with_descriptions.csv")

from langchain_core.documents import Document
docs = [Document(page_content=row["Description"]) for _, row in df.iterrows()]

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma.from_documents(docs, embeddings, persist_directory="chroma_db")

searched = vector_store.similarity_search("주차와 흡연이 가능한 맛집은?", k=3)
print(searched)
