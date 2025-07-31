# pip install sentence-transformers
from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

docs = [
    "한국의 수도는 서울입니다.",
    "중국의 수도는 북경입니다.",
    "삼성전자의 본사는 수원에 있습니다.",
    "파이썬은 프로그래밍 언어입니다.",
]
query = "한국의 수도는?"

embedded_docs = embeddings.embed_documents(docs)
embedded_query = embeddings.embed_query(query)

from sklearn.metrics.pairwise import cosine_similarity
similarity = cosine_similarity([embedded_query], embedded_docs)
print(similarity)	# [[0.77902504 0.65345867 0.45218245 0.33220978]]
