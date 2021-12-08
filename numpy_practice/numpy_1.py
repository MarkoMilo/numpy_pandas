import numpy as np

red = [[1, 2, 3, 4, 5],
       {'marko': 1},
       (1, 3, 4)
]

for i in red:
    arr = np.array(i)
    print("array: ", arr)
    print("Dimension of array: ", arr.ndim)

# Numpy data types
arr = np.array([1, 2, 3, 4])
print(arr.dtype)

arr = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

arr = np.array([1, 2, 3, 4], dtype='i2')
print(arr)
print(arr.dtype)

arr = np.array([1.1, 2.1, 3.1])
print(arr)
print(arr.dtype)
newarr = arr.astype(int)
print(newarr)
print(newarr.dtype)

# NUMPY ARRAY COPY VS VIEW
# THE MAIN DIFFERENCE BETWEEN A COPY AND A VIEW OF AN ARRAY IS THAT THE COPY IS A NEW ARRAY, AND THE VIEW IS JUST A
# VIEW OF THE ORIGINAL ARRAY.

arr = np.array([1, 2, 3, 4, 5])
y = arr.copy()
arr[0] = 42
print(arr)
print(y)

arr = np.array([1, 2, 3, 4, 5])
x = arr.view()
arr[0] = 42
print(arr)
print(x)

arr = np.array([1, 2, 3, 4, 5])
z = arr.view()
z[0] = 31
print(arr)
print(x)

# Check is array owns it's data
print("\n*************************************\n")
print(arr.base)
print(z.base)
print(y.base)

# NUMPY ARRAY SHAPE - tHE NUMBER OF ELEMENTS IN EACH DIMENSION

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8, ]])
print("tHE NUMBER OF ELEMENTS IN EACH DIMENSION", arr.shape)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)


# NUMPY ARRAY RESHAPING
# THE SHAPE OF AN ARRAY IS THE NUMBER OF ELEMENTS IN EACH DIMENSION.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print("/////////////\n",newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = arr.reshape(2, 4).base
print(x, type(x))

y = arr.copy()
yy = arr.reshape(2, 4).base
print(yy, type(yy))

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = arr.reshape(-1, 2, 2)
print(newarr)

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print("******\n",newarr)


"""
* NUMPY ARRAY ITERATING

ITERATING MEANS GOING THROUGH ELEMENTS ONE BY ONE.
AS WE DEAL WITH MULTI-DIMENSIONAL ARRAYS IN NUMPY, WE CAN DO THIS USING BASIC FOR LOOP OF PYTHON.
IF WE ITERATE ON A 1-D ARRAY IT WILL GO THROUGH EACH ELEMENT ONE BY ONE.
"""

arr = np.array([1, 2, 3])
for x in arr:
  print(x)

arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
  print(x)

# Iterating through 3-D array
print("# Iterating through 3-D array\n")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)
    for y in x:
        print(y)
        for z in y:
            print(z)


# nditer()
print("\n\nnditer()\n")

arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for i in np.nditer(arr):
    print("i is: ", i)

arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
  print("********", x)

print("Iterate through every second element using nditer ")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i in np.nditer(arr[:, ::2]):
    print(i)

print("Enumerated Iteration Using ndenumerate(), first element in for is element position, the second is element")
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for i, j in np.ndenumerate(arr):
    print("{}\n{}".format(i, j))

"""
NUMPY JOINING ARRAY
JOINING MEANS PUTTING CONTENTS OF TWO OR MORE ARRAYS IN A SINGLE ARRAY.
IN SQL WE JOIN TABLES BASED ON A KEY, WHEREAS IN NUMPY WE JOIN ARRAYS BY AXES.
"""

print("NUMPY JOINING ARRAY")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

print("\n***************************\n")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

print("\n***************************\n")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

print("\n***************************\n")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.hstack((arr1, arr2))
print(arr)

print("\n***************************\n")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.vstack((arr1, arr2))
print(arr)

print("\n***************************\n")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr3 = np.array([7, 8, 9])
arr = np.dstack((arr1, arr2, arr3))
print(arr)

"""
Splitting NumPy Arrays
We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
"""

print("\n***************************\n")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)

print("\n***************************\n")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 4)
print(newarr)


print("\n***************************\n")
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr[0])
print(newarr[1])
print(newarr[2])

print("\n Split 2-D arrays ***************************\n")
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print(newarr[0])
print(newarr[1])
print(newarr[2])



print("\n***********************************************************\n")
print("\n Split the 2-D array into three 2-D arrays. \n")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)

print("\n***********************************************************")
print("Split the 2-D array into three 2-D arrays along rows.. \n")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)

print("\n***********************************************************")
print("Use the hsplit() method to split the 2-D array into three 2-D arrays along rows. \n")
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

arr = np.array([1,2,3], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)

arr = np.array([1, 2, 3, 4])
print(arr[2] + arr[3])

arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('2nd element on 1st row: ', arr[0, 1])

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])

# Slicing numpy arrays
rr = np.array([[1,2,3,4,5], [6,7,8,9,10]])
print('Last element from 2nd dim: ', rr[1, -1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[-3:-1])

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print("From array: {} show element between element 1 and 5 with step 2: {}".format(arr, arr[1:5:2]))

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[::2])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[1, 1:4])

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[0:2, 2])
# the same results
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(arr[:, 2])