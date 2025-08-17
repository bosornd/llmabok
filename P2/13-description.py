# pip install pandas
import pandas as pd     # Importing pandas for data manipulation

df = pd.read_csv("../data/restaurant_reviews.csv")
print(df)

def generate_description(row):
    description = f"{row['ID']}의 맛에 대한 평가는 {row['Taste']}점입니다.\n"
    return description

# apply the function to each row and create a new column
df["Description"] = df.apply(generate_description, axis=1)

df.to_csv("restaurant_reviews_with_descriptions.csv", index=False)
