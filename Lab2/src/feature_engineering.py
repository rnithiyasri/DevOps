import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("processed.csv")

X = df.drop("MEDV", axis=1)
y = df["MEDV"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

train = X_train.copy()
train["MEDV"] = y_train

test = X_test.copy()
test["MEDV"] = y_test

train.to_csv("train.csv", index=False)
test.to_csv("test.csv", index=False)

print("Feature Engineering Completed")