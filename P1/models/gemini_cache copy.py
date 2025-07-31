from dotenv import load_dotenv
load_dotenv()

# pip install google-genai
from google import genai
client = genai.Client()

file = client.files.upload(file="../../P2/document/AI 에이전트 동향.pdf")
cache = client.caches.create(
    model='gemini-2.0-flash',
    config=genai.types.CreateCachedContentConfig(contents=[file])
)

from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(
    model='gemini-2.0-flash',
    cached_content=cache.name,
)

response = llm.invoke("보고서의 내용을 요약해줘")
print(response.content)
