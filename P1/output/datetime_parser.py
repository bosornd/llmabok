from dotenv import load_dotenv
load_dotenv()

from langchain.output_parsers import DatetimeOutputParser
output_parser = DatetimeOutputParser()
print(output_parser.get_format_instructions())

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("""
{company}의 창립기념일은? 다음 형식으로 답변해 주세요. {format}""")
prompt = prompt.partial(format=output_parser.get_format_instructions())

from langchain.chat_models import init_chat_model
llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")
chain = prompt | llm | output_parser

response = chain.invoke({"company": "삼성"})    # instance of Datetime
print(response.strftime("%Y년 %m월 %d일"))      # Output: 1938년 03월 01일

