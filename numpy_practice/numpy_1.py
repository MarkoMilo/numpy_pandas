import numpy as np

red = [[1, 2, 3, 4, 5],
       {'marko': 1},
       (1, 3, 4)
]

for i in red:
    arr = np.array(i)
    print("array: ", arr)
    print("Dimension of array: ", arr.ndim)

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