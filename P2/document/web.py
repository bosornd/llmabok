import os
os.environ["USER_AGENT"] = "Mozilla/5.0"

import bs4
from langchain_community.document_loaders import WebBaseLoader

loader = WebBaseLoader(
    web_path="https://n.news.naver.com/article/001/0015503871",
    bs_kwargs=dict(
        parse_only=bs4.SoupStrainer("article")  # <article> 태그만 추출
    ),
)

docs = loader.load()
print(docs[0].page_content)
