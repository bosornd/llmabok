import dotenv
dotenv.load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

from typing import TypedDict
class State(TypedDict):
    subject: str
    story: str
    criticism: str
