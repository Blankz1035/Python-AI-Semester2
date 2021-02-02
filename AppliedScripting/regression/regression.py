import pandas as pd
import numpy as np

from matplotlib import pyplot as plt

x = np.array([0,1,2,3,4,5])
y = np.array([0,0.9,0.8,0.1,-0.4,-0.8])

print (x)
print(y)

p1 = np.polyfit(x,y,1)
p2 = np.polyfit(x,y,2)
p3 = np.polyfit(x,y,3)


print (p1)
print (p2)
print (p3)


plt.plot(x,y,'o')

xp = np.linspace(-1,6)

plt.plot(xp,np.polyval(p1,xp), 'r-')
plt.plot(xp,np.polyval(p2,xp), 'b--')
plt.plot(xp,np.polyval(p3,xp), 'g:')

plt.show()

from scipy.stats import linregress
slope, intercept, r_value, p_value, std_err = linregress(x,y)

print(r_value ** 2)
print(p_value)