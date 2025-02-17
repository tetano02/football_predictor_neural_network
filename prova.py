import numpy as np
import pandas as pd

x1 = []
x2 = []
for i in range(2013, 2024):
    data = pd.read_csv(f'file_csv/serie_a_{i}-{(i+1)%2000}.csv')
    x1.append(data['Home Value'].values)
    x2.append(data['Away Value'].values)
    x = [x1, x2]
    y = data['Result']
    print(x.shape())

a = np.array([[1], [2], [3]])
b = np.array([[4], [5], [6]])
c = np.concatenate((a, b), axis=1)
print(c)
c = np.concatenate((c, c), axis=0)
print(c.shape)