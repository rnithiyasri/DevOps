import joblib
import pandas as pd
from sklearn.linear_model import LinearRegression

train = pd.read_csv("train.csv")

X = train.drop("MEDV", axis=1)
y = train["MEDV"]

model = LinearRegression()

model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model Saved")