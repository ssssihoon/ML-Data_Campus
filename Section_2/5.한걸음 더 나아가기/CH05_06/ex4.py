import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])
b = np.reshape(a, (3, 2))

print(b.shape)
print(b)
