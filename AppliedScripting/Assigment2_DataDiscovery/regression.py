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
### Visualization Switch
if 1 == 2:
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
####### Results
#                  Temperature  AmbientPressure  ...  ExhaustVacuum  NetEnergyOutput
# Temperature         1.000000         0.842456  ...      -0.549027        -0.949082
# AmbientPressure     0.842456         1.000000  ...      -0.309473        -0.866988
# RelHumidity        -0.480354        -0.386454  ...       0.081330         0.499157
# ExhaustVacuum      -0.549027        -0.309473  ...       1.000000         0.391671
# NetEnergyOutput    -0.949082        -0.866988  ...       0.391671         1.000000

# Model variables
# y has been set previously.
### Split data to X and Y variables. Y will be explained by the X data.
#x = data[["Temperature", "AmbientPressure", "RelHumidity", "ExhaustVacuum", "NetEnergyOutput"]] # r2  1.0
x = data[["Temperature", "AmbientPressure", "RelHumidity", "ExhaustVacuum"]] # r2  0.9340949633631872
#x = data[["Temperature", "AmbientPressure", "RelHumidity"]]  # r2  0.9214847177606686
#x = data[["Temperature", "AmbientPressure"]] # r2  0.9191244258393328

## Create test and training data.
X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size = 0.33, random_state = 32)

# print(X_train.shape)
# print(X_test.shape)
# print(Y_train.shape)
# print(Y_test.shape)

model = LinearRegression()
model.fit(X_train, Y_train)

## Predictions
Y_Pred = model.predict(X_test)

# Scatter with Line of best fit (1st degree)
plt.scatter(x=Y_test, y=Y_Pred)
m, b = np.polyfit(Y_test, Y_Pred, 1)
#m = slope, b=intercept
plt.plot(Y_test, m*Y_test + b, 'r-')
plt.show()

## Accuracy
rmse = np.sqrt(mean_squared_error(Y_test,Y_Pred))
r2 = r2_score(Y_test,Y_Pred)

# Final output
print()
print ('Best rmse = ', rmse)
print ('Best R2 ', r2)
print("Best Random State: 32")

