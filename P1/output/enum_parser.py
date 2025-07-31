from dotenv import load_dotenv
load_dotenv()

from enum import Enum
class Color(Enum):
    RED    = "빨강"
    BLUE   = "파랑"
    YELLOW = "노랑"

from langchain.output_parsers import EnumOutputParser
output_parser = EnumOutputParser(enum=Color)

print(output_parser.get_format_instructions())

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""{object}의 색깔은? 다음 형식으로 답변해 주세요.
{format}
예시:
  질문: 바나나의 색깔은?
  답변: 노랑
""")
prompt = prompt.partial(format=output_parser.get_format_instructions())

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

response = chain.invoke({"object": "사과"})    # instance of Color
print(response)                               # Output: Color.RED
