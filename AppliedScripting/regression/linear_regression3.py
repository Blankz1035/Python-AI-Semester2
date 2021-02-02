from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import PolynomialFeatures
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([0,0.9,0.8,0.1,-0.4,-0.8])

x = x[:,np.newaxis]
y = y[:,np.newaxis]



poly_features = PolynomialFeatures(degree=2)
poly_features2 = PolynomialFeatures(degree=3)


xTrans = poly_features.fit_transform(x)
xTrans2 = poly_features2.fit_transform(x)

plt.scatter(x,y)

plt.show()

model = LinearRegression()
model2 = LinearRegression()
model3 = LinearRegression()

model.fit(x,y)

model2.fit(xTrans, y)

model3.fit(xTrans2, y)

yPred = model.predict(x)

yPred2 = model2.predict(xTrans)

yPred3 = model3.predict(xTrans2)

#print(y)
#print(yPred2)
#print(yPred3)


rmse = np.sqrt(mean_squared_error(y,yPred))

r2 = r2_score(y,yPred)

print('Linear')
print ('rmse = ', rmse)
print ('r2 ', r2)

print('-'*10)

rmse = np.sqrt(mean_squared_error(y,yPred2))

r2 = r2_score(y,yPred2)

print('Poly 2')
print ('rmse = ', rmse)
print ('r2 ', r2)

print('-'*10)

rmse = np.sqrt(mean_squared_error(y,yPred3))

r2 = r2_score(y,yPred3)

print('Poly 3')
print ('rmse = ', rmse)
print ('r2 ', r2)


plt.scatter(x,y)
plt.plot(x,yPred, 'r-')
plt.plot(x,yPred2, 'b--')
plt.plot(x,yPred3, 'g:')

plt.show()