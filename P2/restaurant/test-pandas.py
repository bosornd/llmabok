import pandas as pd

df = pd.DataFrame([{'Name': 'Alice', 'Age': 25},
                   {'Name': 'Bob', 'Age': 30}])
print(df)

row = df.iloc[0]
print(row)
print(type(row))
print(row["Name"])
print(row["Age"])
print(row.index)
print(row.values)

for index, row in df.iterrows():
    print(row)

for index, row in df.iterrows():
    for key in row.index:
        print(f"  {key}: {row[key]}")