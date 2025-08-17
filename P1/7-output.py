import dotenv
dotenv.load_dotenv()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("{country}의 수도는?")

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm

response = chain.invoke("중국")
print(response.content)


