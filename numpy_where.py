import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],
                  [11, 12, 13, 14, 15]])


print(np.where(array % 2 == 0, array, 0))
print(np.where(array < 10, array , 0))
