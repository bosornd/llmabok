with open("AI 에이전트 동향-1.txt", "r", encoding="utf-8") as f:
    file = f.read()

# from langchain_google_genai import GoogleGenerativeAIEmbeddings
# embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")

from langchain_huggingface import HuggingFaceEmbeddings
embeddings = HuggingFaceEmbeddings(model_name="Qwen/Qwen3-Embedding-0.6B")

# pip install langchain_experimental
from langchain_experimental.text_splitter import SemanticChunker
splitter = SemanticChunker(embeddings,
                           breakpoint_threshold_type="percentile",
                           breakpoint_threshold_amount=50,
#                           breakpoint_threshold_type="standard_deviation",
#                           breakpoint_threshold_amount=3.0,
#                           breakpoint_threshold_type="interquartile",
#                           breakpoint_threshold_amount=1.5,
#                           breakpoint_threshold_type="gradient",
#                           breakpoint_threshold_amount=95,
                          )
docs = splitter.create_documents([file])

print(f"Number of splitted documents: {len(docs)}")
for doc in docs:
    print(f"\n\n---\n\n{doc.page_content}")
