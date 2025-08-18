from dotenv import load_dotenv
load_dotenv()

from pydantic import BaseModel, Field
class Capital(BaseModel):
    country: str = Field(description="국가")
    capital: str = Field(description="수도")

from langchain_core.output_parsers import JsonOutputParser
output_parser = JsonOutputParser(pydantic_object=Capital)

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
{country}의 수도는? 다음 형식으로 답변해 주세요.
{format}
""")

prompt = prompt.partial(format=output_parser.get_format_instructions())
prompt.pretty_print()

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

response = chain.invoke({"country": "한국"})
print(type(response))    # <class 'dict'>

print(response)

import json
print(json.dumps(response, indent=2, ensure_ascii=False))
