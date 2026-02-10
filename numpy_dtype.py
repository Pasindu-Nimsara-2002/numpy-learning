import numpy as np

array = np.array([[[1,2,3], [4,5,6], [7,8,9], [10,11,12]],
                  [[13,14,15],[16,17,18], [19,20,21], [22,23,24]]], dtype=np.float64)

print(f"Array:\n{array}")
print(f"Data type: {array.dtype}")

array_int = array.astype(np.int32)
print(f"\nArray with int32 data type:\n{array_int}")
print(f"Data type of the new array: {array_int.dtype}")