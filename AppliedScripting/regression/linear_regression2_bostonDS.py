from sklearn.datasets import load_boston
import pandas as pd

boston = load_boston()

#print(boston.keys())
#print(boston.data.shape)
#print(boston.feature_names)

#print (boston.DESCR)

df = pd.DataFrame(boston['data'], columns=boston['feature_names'])

df['MEDV'] = boston['target']

df.dtypes

df.isnull().value_counts()

df.describe()

import matplotlib.pyplot as plt
import seaborn as sns

sns.displot(df['MEDV'], bins=30)
plt.show()



ax = sns.heatmap(df[['RM','AGE', 'TAX','LSTAT', 'MEDV']].corr(),
cmap=sns.cubehelix_palette(20, light=0.95, dark=0.15))
ax.xaxis.tick_top() # move labels to the top


df[['RM','AGE', 'TAX','LSTAT', 'MEDV']].corr()

sns.pairplot(df[['RM','AGE', 'TAX','LSTAT', 'MEDV']],
plot_kws={'alpha': 0.6},
diag_kws={'bins': 30})
plt.show()


_, ax = plt.subplots(1, 2)
plt.subplots_adjust(left=None, bottom=None, right=None, top=None, wspace=.5, hspace=None)
sns.regplot(x='RM', y='MEDV', data=df, ax=ax[0],
scatter_kws={'alpha': 0.4}, color='b')
sns.regplot(x='LSTAT', y='MEDV', data=df, ax=ax[1],
scatter_kws={'alpha': 0.4}, color='r')