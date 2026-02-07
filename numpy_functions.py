import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15]])

print(np.shape(array))

print(np.sum(array, axis=0))  # Sum along columns
print(np.sum(array, axis=1))  # Sum along rows
print(np.mean(array, axis=0))  # Mean along columns
print(np.mean(array, axis=1))  # Mean along rows
