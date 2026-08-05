import pandas as pd

df = pd.read_csv("raw.csv")

df = df.drop_duplicates()
df = df.fillna(df.median(numeric_only=True))

df.to_csv("processed.csv", index=False)

print("Data Preprocessing Completed")