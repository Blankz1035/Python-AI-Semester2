from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.model_selection import train_test_split

import seaborn as sns

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
print("Correlation between values:")
print(data.corr())

## Begin modeling

# Our dependent variable is the netenergeyoutput of the DF.
y = data.NetEnergyOutput


# Visualization
sns.displot(y, bins=30)
plt.show()

ax = sns.heatmap(data.corr(),
cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))
ax.xaxis.tick_top() # move labels to the top

sns.pairplot(data,
plot_kws={'alpha': 0.6},
diag_kws={'bins': 30})
plt.show()

# The visualization indicates that we have correlation between the following:
# NEO and Temperature
# AmbientPressure and Temp
# NEO  and AmbientPressure
####### Results
#                  Temperature  AmbientPressure  ...  ExhaustVacuum  NetEnergyOutput
# Temperature         1.000000         0.842456  ...      -0.549027        -0.949082
# AmbientPressure     0.842456         1.000000  ...      -0.309473        -0.866988
# RelHumidity        -0.480354        -0.386454  ...       0.081330         0.499157
# ExhaustVacuum      -0.549027        -0.309473  ...       1.000000         0.391671
# NetEnergyOutput    -0.949082        -0.866988  ...       0.391671         1.000000



