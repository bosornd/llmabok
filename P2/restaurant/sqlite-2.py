from dotenv import load_dotenv
load_dotenv()

from sqlalchemy import create_engine
engine = create_engine("sqlite:///restaurant.db")

from langchain_community.utilities import SQLDatabase
db = SQLDatabase(engine=engine)

print(db.dialect)                   # sqlite
print(db.get_usable_table_names())  # ['restaurant']
print(db.get_table_info())

# searched = db.run("SELECT ID FROM restaurant WHERE Parking='yes' and Taste >= 80;")
searched = db.run("SELECT ID, Taste, Parking FROM restaurant WHERE Smoking_Area='yes' and Parking='yes' ORDER BY Taste DESC LIMIT 3;")
print(eval(searched))       # searched가 문자열이다.

from langchain import hub
prompt = hub.pull("rlm/text-to-sql")
prompt = prompt.partial(table_info=db.get_table_info(), dialect=db.dialect, 
                        few_shot_examples="")

from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash")

chain = prompt | llm

response = chain.invoke("흡연 구역과 주차장이 있고 맛 평가가 높은 식당을 3개 찾아줘.")
print(response.content)
"""
SQLQuery: SELECT ID FROM restaurant WHERE Smoking_area = 'yes' AND Parking = 'yes' ORDER BY Taste DESC LIMIT 3
SQLResult: REST_018
REST_003
REST_012
Answer: REST_018
REST_003
REST_012
"""