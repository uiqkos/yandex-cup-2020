#%%
import random
import numpy as np
import seaborn
import pandas
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

#%%
Stumper = __import__("A_Stump", fromlist=['mse', 'smse', 'stump'])


X = []
Y = []
Z = []
stump, mse, smse = Stumper.stump, Stumper.mse, Stumper.smse
for test_num in range(100):
    pair_count = random.randint(1, 1000)
    pairs = [
        (x, y) for x, y in zip(
            np.linspace(0, 100, pair_count),
            [random.uniform(0, 100) for i in range(pair_count)]
        )
    ]
    a, b, c, smse_, mse_ = stump(pairs)

    print(smse_, mse_)

    # smse = a * mse + b * pair_count + c
    # X.append((mse_, pair_count))
    X.append(mse_)
    Y.append(smse_)

data = pandas.DataFrame({'X': X, 'Y': Y})

#%%
print(data)
seaborn.lineplot(data=data, x='X', y='Y')
plt.show()

#%%
print(np.array(X), np.array(Y))
model = LinearRegression()
model.fit(np.array(X), data['Y'])

#%%
print(model.coef_)