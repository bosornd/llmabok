import pandas as pd
df = pd.read_csv('restaurant_reviews.csv')

from sqlalchemy import create_engine
engine = create_engine("sqlite:///restaurant.db")
df.to_sql("restaurant", engine, if_exists="replace", index=False)
