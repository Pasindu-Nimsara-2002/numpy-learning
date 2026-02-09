import numpy as np

array = np.array([[1, 2, 3, 4, 5],
                  [6, 7, 8, 9, 10],         
                  [11, 12, 13, 14, 15]])


array_reshaped = array.reshape(5,3)

print(array_reshaped)
print(array.reshape(-1, 5))  # Automatically determine the number of rows
print(array.reshape(3, -1))  # Automatically determine the number of columns