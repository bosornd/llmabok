from langchain_community.document_loaders import WebBaseLoader

import bs4
loader = WebBaseLoader("https://news.naver.com/article/001/0015568637")

docs = loader.load()
print(docs)