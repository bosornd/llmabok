from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("AI 에이전트 동향.pdf", mode="single")
docs = loader.load()

with open("AI 에이전트 동향.txt", "w", encoding="utf-8") as f:
    f.write(docs[0].page_content)
