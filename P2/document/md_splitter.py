with open("langchain.md", "r", encoding="utf-8") as f:
    file = f.read()

from langchain_text_splitters import MarkdownHeaderTextSplitter
splitter = MarkdownHeaderTextSplitter(
             headers_to_split_on=[("#", "Chapter"), ("##", "Section")],
             strip_headers=False,
)

docs = splitter.split_text(file)

print(f"Number of splitted documents: {len(docs)}")
for doc in docs:
    print(f"\n\n---\n\n{doc.page_content}")
