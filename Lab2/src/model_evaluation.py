import json
import joblib
import pandas as pd
from sklearn.metrics import mean_squared_error, r2_score

test = pd.read_csv("test.csv")

X = test.drop("MEDV", axis=1)
y = test["MEDV"]

model = joblib.load("model.pkl")

pred = model.predict(X)

metrics = {
    "RMSE": mean_squared_error(y, pred) ** 0.5,
    "R2": r2_score(y, pred)
}

with open("metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)

print(metrics)