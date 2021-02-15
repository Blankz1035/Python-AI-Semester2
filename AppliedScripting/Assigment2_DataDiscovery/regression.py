from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt


try:
    data = pd.read_csv("./data/p1ml.csv")

except FileNotFoundError:
    print("File not found at target location.")
    exit(0)

# File has been found, now continue with regression.

print(data.head())

