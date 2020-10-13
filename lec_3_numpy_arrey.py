import numpy as np
A = np.zeros((2,3))
print(A)

A[0, 2] = 5
print(A)

B = np.ones((3, 2))
print(B)

A = np.ndarray(shape=(10, 2))
print(A)

A = np.arange(0, 5, 0.5)
print(A)
print(len(A))