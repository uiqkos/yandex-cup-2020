
def get_data(path='C:\\Users\\uiqko\\GoogleDrive\\code\\python\\yandex-cup-2020\\Machine-learning\\train.in'):
    file = open(path, 'r')
    line_count = int(file.readline())

    data = {'id': [], 'ans': []}
    for i in range(42):
        data[f't{str(i)} x'] = []
        data[f't{str(i)} y'] = []

    for line in file.readlines():
        line = line.split()
        data['id'].append(int(line[0]))
        data['ans'].append(int(line[1]))

        k = int(line[2])
        j = 3
        for i in range(k):
            data[f't{str(i)} x'].append(float(line[j + i]))
            data[f't{str(i)} y'].append(float(line[j + 1 + i]))
            j += 2
    return data

def get_data_test(path='C:\\Users\\uiqko\\GoogleDrive\\code\\python\\yandex-cup-2020\\Machine-learning\\test.in'):
    file = open(path, 'r')
    line_count = int(file.readline())

    data = {'id': []}
    for i in range(42):
        data[f't{str(i)} x'] = []
        data[f't{str(i)} y'] = []

    for line in file.readlines():
        line = line.split()
        data['id'].append(int(line[0]))

        k = int(line[1])
        j = 2
        for i in range(k):
            data[f't{str(i)} x'].append(float(line[j + i]))
            data[f't{str(i)} y'].append(float(line[j + 1 + i]))
            j += 2
    return data

#%%

train = get_data()
test = get_data_test()

#%%
import pandas as pd
train = get_data()
train['t41 x'].append(train['t40 x'][0])
train['t41 y'].append(train['t40 y'][0])
train['t41 x'].append(train['t41 x'][0])
train['t41 y'].append(train['t41 y'][0])
train = pd.DataFrame(train)
train.set_index('id', drop=True, inplace=True)

X_train = train.drop('ans', axis=1)
y_train = train['ans']

#%%
for i in range(5):
    test['t41 x'].append(test['t40 x'][0])
    test['t41 y'].append(test['t40 y'][0])
X_test = pd.DataFrame(test)
X_test.set_index('id', drop=True, inplace=True)

#%%
from sklearn.manifold import TSNE
import pylab

tsne = TSNE()
new_x = tsne.fit_transform(X_train, y_train)
#%%
pylab.figure(figsize=(10, 6))
pylab.scatter(new_x[:, 0], new_x[:, 1], c=y_train, alpha=0.4)
pylab.show()

#%%
import random

someone = train.iloc[random.randint(0, len(train)), :]
x_someone = [someone[i] for i in range(1, len(someone), 2)]
y_someone = [someone[i] for i in range(2, len(someone), 2)]

pylab.scatter(x_someone, y_someone)
pylab.show()
#%%
from sklearn.ensemble import RandomForestClassifier
model = RandomForestClassifier(n_estimators=100, max_depth=3, criterion='entropy', max_features=10)
model.fit(X_train, y_train)

#%%
predictions = pd.DataFrame({'id': X_test.index, 'ans': model.predict(X_test)}, index=None)
predictions.to_csv('Predictions.csv', sep=' ', index=False)

#%%
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

#%%
predictions = pd.DataFrame({'id': X_test.index, 'ans': model.predict(X_test)}, index=None)
predictions.to_csv('Predictions.csv', sep=' ', index=False, header=False)

#%%
from sklearn.neighbors import KNeighborsClassifier
model = KNeighborsClassifier()
model.fit(X_train, y_train)
#%%
predictions = pd.DataFrame({'id': X_test.index, 'ans': model.predict(X_test)}, index=None)
predictions.to_csv('Predictions.csv', sep=' ', index=False, header=False)

#%%
from sklearn.svm import SVC
model = SVC()
model.fit(X_train, y_train)
#%%
predictions = pd.DataFrame({'id': X_test.index, 'ans': model.predict(X_test)}, index=None)
predictions.to_csv('Predictions.csv', sep=' ', index=False, header=False)


