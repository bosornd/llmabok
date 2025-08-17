import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("{country}의 수도는?")
print(prompt)
