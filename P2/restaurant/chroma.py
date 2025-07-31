from dotenv import load_dotenv
load_dotenv()

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

from langchain_chroma import Chroma
vector_store = Chroma(embedding_function=embeddings, persist_directory="chroma_db")

searched = vector_store.similarity_search(
               "흡연 구역과 주차장이 있고 맛 평가가 80점 이상인 식당을 추천해줘.", k=3)
print(searched)

searched = vector_store.similarity_search(
               "흡연 구역과 주차장이 있는 식당을 알려줘.", k=3,
               filter={"Taste": {"$gte": 80}})
print(searched)

searched = vector_store.get(
    where={"$and": [{"Smoking_area": "yes"},
                    {"Parking": "yes"},
                    {"Taste": {"$gte": 80}}]},
)
print(searched)
for m in searched["metadatas"]: print(m)
