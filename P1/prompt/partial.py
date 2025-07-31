from dotenv import load_dotenv
load_dotenv()

from langchain_core.prompts import PromptTemplate
prompt = PromptTemplate.from_template("생일이 {date}인 유명인을 {n}명 알려줘.")
print(prompt.invoke({"date":"7월 1일", "n":1}))

from datetime import datetime
prompt = prompt.partial(date=datetime.now().strftime("%m월 %d일"))
print(prompt)
prompt.pretty_print()       # 생일이 07월 29일인 유명인을 {n}명 알려줘.

prompt = PromptTemplate(
            template="생일이 {date}인 유명인을 {n}명 알려줘.",
            input_variables=["n"],
            partial_variables={"date":datetime.now().strftime("%m월 %d일")}
         )

print(prompt.invoke({"n":2}))
print(prompt.invoke({"date":"7월 2일", "n":3}))

