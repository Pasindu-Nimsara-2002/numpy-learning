import numpy as np

ages = np.array([[25, 30, 35, 40, 45],
                 [50, 55, 60, 65, 70]])

teens = ages[ages <= 19]
adults = ages[(ages > 19) & (ages < 65)]
elders = ages[ages >= 65]

print("Teens:", teens)
print("Adults:", adults)
print("Elders:", elders)