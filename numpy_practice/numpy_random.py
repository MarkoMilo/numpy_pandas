import numpy as np
from numpy import random


print("\n******************************************************")
print("Print random float element \n")
x = random.rand()
print(x)


print("\n******************************************************")
print(" Create random 'size=n' element in range from 67 to 100\n")
x = random.randint(67, 100, size=5)
print(x)

print("\n******************************************************")
print(" Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100:\n")
x = random.randint(0, 100, size=(3, 5))
print(x)

print("\n******************************************************")
print("Generate a 1-D array containing 5 random floats: \n")
x = random.rand(5)
print(x)

print("\n******************************************************")
print("Generate a 2-D array with 3 rows, each row containing 5 random FLOAT numbers: \n")
x = random.rand(3, 5)
print(x)

print("\n******************************************************")
print("Return one of the values in an array: \n")
x = random.choice([3, 5, 7, 9])
print(x)

print("\n******************************************************")
print("Generate a 2-D array that consists of the values in the array parameter (3, 5, 7, and 9): \n")
x = random.choice([3, 5, 7, 9], size=(3, 5))
print(x)

# RANDOM DATA DISTRIBUTION
"""
What is Data Distribution?
Data Distribution is a list of all possible values, and how often each value occurs.
Such lists are important when working with statistics and data science.
The random module offer methods that returns randomly generated data distributions.
"""

print("\n******************************************************")
print("Generate a 1-D array containing 100 values, where each value has to be 3, 5, 7 or 9.\nThe probability for the "
      "value to be 3 is set to be 0.1\nThe probability for the value to be 5 is set to be 0.3\nThe probability for "
      "the value to be 7 is set to be 0.6\nThe probability for the value to be 9 is set to be 0 \n")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(100))
print(x)

print("\n******************************************************")
print("Same example as above, but return a 2-D array with 3 rows, each containing 5 values. \n")
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(4, 4))
print(x)

# RANDOM PERMUTATIONS OF ELEMENTS
"""
A permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
The NumPy Random module provides two methods for this: shuffle() and permutation().
"""

print("\n******************************************************")
print("Shuffle means changing arrangement of elements in-place. i.e. in the array itself. \n")
arr = np.array([1, 2, 3, 4, 5])
print("array before shuffle: ", arr)
random.shuffle(arr)
print("array after shuffle: ", arr)

# SEABORN - library for data vizualizatin
"""
Visualize Distributions With Seaborn
Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.
"""
import matplotlib.pyplot as plt
import seaborn as sns


print("\n******************************************************")
print("seaborn \n")
sns.distplot([0, 1, 2, 3, 4, 5], hist=False)
# plt.show()

# NORMAL (GAUSSIAN) DISTRIBUTION
"""
The Normal Distribution is one of the most important distributions.
It is also called the Gaussian Distribution after the German mathematician Carl Friedrich Gauss.
It fits the probability distribution of many events, eg. IQ Scores, Heartbeat etc.
Use the RANDOM.NORMAL() method to get a Normal Data Distribution.
It has three parameters:
      loc - (Mean) where the peak of the bell exists.
      scale - (Standard Deviation) how flat the graph distribution should be.
      size - The shape of the returned array.
"""


print("\n******************************************************")
print(" \n")
x = random.normal(size=(2, 3))
print(x)

print("\n******************************************************")
print("Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2: \n")
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)

print("\n******************************************************")
print(" \n")
sns.distplot(random.normal(size=1000), hist=False)
plt.show()


# print("\n******************************************************")
# print(" \n")
#
#
#
# print("\n******************************************************")
# print(" \n")
#
#
#
# print("\n******************************************************")
# print(" \n")
#
#
#
# print("\n******************************************************")
# print(" \n")



