import numpy as np
from sklearn.linear_model import LinearRegression
a, b = [15, 12,  8,  8,  7,  7,  7,  6, 5,  3],[10, 25, 17, 11, 13, 17, 20, 13, 9, 15]
a = np.array(a).reshape(-1, 1)
b = np.array(b).reshape(-1, 1)

model = LinearRegression()
model.fit(a, b)
print("{0:.1f}".format(float(model.predict(10))))
