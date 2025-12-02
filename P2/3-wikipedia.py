import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

# pip install wikipedia
from langchain_community.retrievers import WikipediaRetriever
retriever = WikipediaRetriever()
