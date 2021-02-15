from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split


## File input via CSV
try:
    data = pd.read_csv("./data/p1ml.csv")

except FileNotFoundError:
    print("File not found at target location.")
    exit(0)

###### File has been found, now continue with regression.

## Data manipulation -> change column names to make more meaningful
data.columns = ["Temperature", "AmbientPressure", "RelHumidity", "ExhaustVacuum", "NetEnergyOutput"]

# Quick Inspection of data
print("Head Inspection of Data Frame:")
print(data.head())
print("Data Frame component details (describe()):")
print(data.describe())
print("Standard Deviations:")
print(data.std())

print()

## Begin modeling





