from dotenv import load_dotenv
load_dotenv()

from langchain.chat_models import init_chat_model

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")

response = llm.invoke("한국의 수도는?")
print(type(response))   # langchain_core.messages.ai.AIMessage
print(response)
# content='한국의 수도는 서울입니다.' additional_kwargs={} response_metadata={'prompt_feedback': {'block_reason': 0, 'safety_ratings': []}, 'finish_reason': 'STOP', 'model_name': 'gemini-2.0-flash', 'safety_ratings': []} id='run--eae1140b-43c9-4815-8bec-f74332d2609a-0' usage_metadata={'input_tokens': 6, 'output_tokens': 9, 'total_tokens': 15, 'input_token_details': {'cache_read': 0}}
