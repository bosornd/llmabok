import pandas as pd
df = pd.read_csv("restaurant_reviews_with_descriptions.csv")

from langchain_core.documents import Document
docs = [Document(page_content=row["Description"],
                 metadata={key: row[key] for key in row.index 
                                         if key != "Description"})
        for _, row in df.iterrows()]
# print(docs[0])

from langchain_huggingface import HuggingFaceEmbeddings
embedding = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma.from_documents(docs, embedding, persist_directory="chroma_db")

retriever = vector_store.as_retriever()
print(retriever.invoke("주차와 흡연이 가능한 맛집은?"))