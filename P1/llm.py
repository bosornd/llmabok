import dotenv
dotenv.load_dotenv()

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

response = llm.invoke("한국의 수도는?")
print(response)

response = llm.invoke("한국의 수도는? 인구, 면적, 기후 등 추가 정보도 알려줘.")
print(response.content)

response = llm.invoke("중국의 수도는? 인구, 면적, 기후 등 추가 정보도 알려줘.")
print(response.content)

response = llm.invoke("한국의 대통령은?")
print(response.content)

