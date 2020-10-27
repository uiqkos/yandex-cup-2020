#%%
import numpy as np
from pandas import DataFrame
from sklearn.linear_model import LinearRegression
import random

#%%
def mse(X, y):
    return np.sum((X - y) ** 2) / len(X)

def smse(X, y):
    return np.sqrt(np.sum((X - y) ** 2) / len(X))

#%%
def get_coef():
    SMSE = []
    N = []
    MSE = []
    for test_num in range(100):
        n = random.randint(1, 10_000)
        X_ = np.linspace(0, 500, n)
        y_ = np.array([random.uniform(0, 100) for i in range(n)])
        SMSE.append(smse(X_, y_))
        # N.append(n)
        MSE.append((mse(X_, y_), n))

    model = LinearRegression()
    model.fit(np.array(MSE), SMSE)
    return model.coef_
#%%
coefs = [get_coef() for i in range(1_000)]

#%%
mean_coef_0 = sum([coefs[i][0] for i in range(len(coefs))]) / len(coefs)
mean_coef_1 = sum([coefs[i][1] for i in range(len(coefs))]) / len(coefs)
print(mean_coef_0, mean_coef_1)
