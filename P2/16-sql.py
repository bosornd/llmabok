import pandas as pd     # Importing pandas for data manipulation
df = pd.read_csv('../data/restaurant_reviews.csv')

from sqlalchemy import create_engine
engine = create_engine("sqlite:///restaurant.db")

df.to_sql("restaurant", engine, if_exists="replace", index=False)

from langchain_community.utilities import SQLDatabase
db = SQLDatabase(engine=engine)

print(db.dialect)                   # sqlite
print(db.get_usable_table_names())  # ['restaurant']
print(db.get_table_info())

searched = db.run("SELECT * FROM restaurant WHERE Smoking_Area='yes' and Parking='yes' and Taste >= 80;")
print(eval(searched))       # searched가 문자열이다.