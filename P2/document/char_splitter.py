with open("AI 에이전트 동향.txt", "r", encoding="utf-8") as f:
    file = f.read()

from langchain_text_splitters import RecursiveCharacterTextSplitter
splitter = RecursiveCharacterTextSplitter()
                # separators = ["\n\n", "\n", " ", ""]

docs = splitter.create_documents([file])

with open("AI 에이전트 동향_Splitted.txt", "w", encoding="utf-8") as f:
    f.write(f"Number of splitted documents: {len(docs)}")
    for doc in docs:
        f.write(f"\n\n---\n\n{doc.page_content}")
