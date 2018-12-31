# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:47:43 2018

@author: Admin
"""

import numpy as np
np_array_1d = np.array([0,2,4,6,8,10])

print(np_array_1d)
[ 0  2  4  6  8 10]
print(np.sum(np_array_1d))
30
np_array_2x3 = np.array([[0,2,4],[1,3,5]])

print(np_array_2x3)
[[0 2 4]
 [1 3 5]]
print(np.sum(np_array_2x3))
15
np_array_2x3 = np.array([[0,2,4],[1,3,5]])

print(np_array_2x3)
 [[0 2 4]
 [1 3 5]]
print(np.sum(np_array_2x3, axis = 0))
[1 5 9]
print(np.sum(np_array_2x3, axis = 1))
[6 9]
print(np.minimum([2, 3, 4], [1, 5, 2]))
[1 3 2]
print(np.maximum([2, 3, 4], [1, 5, 2]))
[2 5 4]
a = np.array([[1,2,3], [4,5,6]])

print(a)
[[1 2 3]
 [4 5 6]]
print(np.cumsum(a))
[ 1  3  6 10 15 21]
print(np.cumsum(a, dtype=float)) 
[ 1.  3.  6. 10. 15. 21.]
print(np.cumsum(a,axis=0)) 
[[1 2 3]
 [5 7 9]]
print(np.cumsum(a,axis=1)) 
[[ 1  3  6]
 [ 4  9 15]]
a = np.array([[1, 2], [3, 4]])

print(np.mean(a))
2.5
print(np.mean(a, axis=0))
[2. 3.]
print(np.mean(a, axis=1))
[1.5 3.5]
print(np.mean(a, dtype=np.float64))
2.5
a = np.array([[10, 7, 4], [3, 2, 1]])

print(np.median(a))
3.5
print(np.median(a, axis=0))
[6.5 4.5 2.5]
print(np.median(a, axis=1))
[7. 2.]
a = np.array([[1, 2], [3, 4]])

print(np.std(a))
1.118033988749895
print(np.std(a, axis=0))
[1. 1.]
print(np.std(a, axis=1))
[0.5 0.5]
print( np.std(a, dtype=np.float64))
 1.118033988749895
 
