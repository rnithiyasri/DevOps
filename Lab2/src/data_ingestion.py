import pandas as pd

df = pd.read_csv("HousingData.csv")
df.to_csv("raw.csv", index=False)

print("Data Ingestion Completed")