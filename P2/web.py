from langchain_community.document_loaders import WebBaseLoader

import bs4
loader = WebBaseLoader("https://news.naver.com/article/001/0015568637",
                       bs_kwargs=dict(parse_only=bs4.SoupStrainer("article")))  # <article> 태그만 추출

docs = loader.load()
print(docs)