import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor, KNeighborsClassifier
from sklearn.metrics import accuracy_score, mean_squared_error, r2_score
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split, cross_val_score

boston = load_boston()

x = boston.data
y = boston.target

# Categories
cats = pd.qcut(y, 5) # data binning into categories to observe category possibilities.
print(cats) # Print the categories that pandas have located from dependent variable
print(cats.value_counts()) # Distribution across the bins

# Create a DF with 1 column and the y values.
y_df = pd.DataFrame(y, columns={"Nums"})
print(y_df)

# Create a new column:
y_df.loc[(y_df["Nums"] < 10), "Cats"] = "low"
y_df.loc[(y_df["Nums"] > 20), "Cats"] = "high"
y_df.loc[(y_df["Nums"] >= 10) & (y_df["Nums"] <= 20), "Cats"] = "med"
print(y_df)


x_train, x_test, y_train, y_test = train_test_split(x,y,test_size=.33, random_state=32)

model = KNeighborsRegressor(n_neighbors=7)
model.fit(x_train, y_train)

# Accuracy
score = model.score(x_test, y_test)

print("Continuous Accuracy = ", score)  # = ~0.55%

## How do we make this better?  We should create categories and compare the results.
x_train, x_test, y_train, y_test = train_test_split(x,y_df["Cats"],test_size=.33, random_state=32)

model2 = KNeighborsClassifier(n_neighbors=7)
model2.fit(x_train, y_train)
score2 = model2.score(x_test, y_test)
print("Categorical Score = ", score2)  # ~0.70%