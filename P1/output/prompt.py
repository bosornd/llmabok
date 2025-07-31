from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
{country}의 수도는? 다음 JSON 형식으로 응답하세요.
Remove Markdown code block markers.
출력 예시:
{{"나라": "한국", "수도": "서울"}}""")

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm

response = chain.invoke({"country": "중국"})
print(response)

import json
parsed = json.loads(response.content)
print(json.dumps(parsed, indent=2, ensure_ascii=False))