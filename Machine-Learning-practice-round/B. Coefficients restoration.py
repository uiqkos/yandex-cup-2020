#%%
import numpy as np
from numpy import sin, log, sqrt
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

data = pd.read_csv('C:/Users/uiqko/GoogleDrive/code/python/yandex-cup-2020/Machine-Learning-practice-round/data.csv', header=None)

#%%
data.head(5)

#%%
plt.scatter(x=data[0], y=data[1])
plt.show()

#%%

X = np.array(data[0])
y = np.array(data[1])


#%%

X_features = []
for x in X:
    X_features.append(
        [
            sin(x) ** 2,      # a^2
            log(x)**2,        # b^2
            sin(x) * log(x),  # 2ab
            x**2,             # c
        ]
    )

linear_regression = LinearRegression()

linear_regression.fit(np.array(X_features), y=y)

coefs = linear_regression.coef_
a, b, c = sqrt(coefs[0]), sqrt(coefs[1]), coefs[3]

plt.show()

#%%

print(round(a, 2), round(b, 2), round(c, 2))
