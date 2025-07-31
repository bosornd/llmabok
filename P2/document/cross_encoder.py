docs = [
    "사과는 빨간색도 있고, 초록색도 있습니다. 나는 빨간 사과는 좋아하지만 초록 사과는 싫어합니다.",
    "바나나는 노란색입니다. 바나나는 맛있습니다. 나는 바나나를 좋아합니다.",
    "포도는 보라색입니다. 포도는 작고 달콤합니다. 포도는 씨가 있어서 먹기 불편합니다. 나는 포도를 싫어합니다.",
    "나는 낚시를 좋아합니다. 낚시는 물고기를 잡는 재미가 있습니다. 낚시는 자연과 함께하는 활동입니다.",
    "나는 여행을 좋아합니다. 여행을 통해 다양한 과일을 맛볼 수 있습니다.",
]
query = "나는 어떤 과일을 좋아할까요?"

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

embedded_docs = embeddings.embed_documents(docs)
embedded_query = embeddings.embed_query(query)

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity([embedded_query], embedded_docs)
print(similarity)	# [[0.55698963 0.5663047  0.40962184 0.36441478 0.60168513]]

from langchain_community.cross_encoders import HuggingFaceCrossEncoder
cross_encoder = HuggingFaceCrossEncoder(model_name="BAAI/bge-reranker-v2-m3")
scores = cross_encoder.score([(query, doc) for doc in docs])
print(scores)       # [1.8223585e-01 2.8320479e-01 3.9508939e-04 1.7941722e-05 6.6267163e-02]
