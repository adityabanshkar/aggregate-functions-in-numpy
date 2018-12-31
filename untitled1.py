# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 09:47:43 2018

@author: Admin
"""

import numpy as np
np_array_1d = np.array([0,2,4,6,8,10])

print(np_array_1d)

print(np.sum(np_array_1d))

np_array_2x3 = np.array([[0,2,4],[1,3,5]])

print(np_array_2x3)

print(np.sum(np_array_2x3))

np_array_2x3 = np.array([[0,2,4],[1,3,5]])

print(np_array_2x3)
 
print(np.sum(np_array_2x3, axis = 0))

print(np.sum(np_array_2x3, axis = 1))

print(np.minimum([2, 3, 4], [1, 5, 2]))

print(np.maximum([2, 3, 4], [1, 5, 2]))

a = np.array([[1,2,3], [4,5,6]])

print(a)

print(np.cumsum(a))

print(np.cumsum(a, dtype=float)) 

print(np.cumsum(a,axis=0)) 

print(np.cumsum(a,axis=1)) 

a = np.array([[1, 2], [3, 4]])

print(np.mean(a))

print(np.mean(a, axis=0))

print(np.mean(a, axis=1))

print(np.mean(a, dtype=np.float64))

a = np.array([[10, 7, 4], [3, 2, 1]])

print(np.median(a))

print(np.median(a, axis=0))

print(np.median(a, axis=1))

a = np.array([[1, 2], [3, 4]])

print(np.std(a))

print(np.std(a, axis=0))

print(np.std(a, axis=1))

print( np.std(a, dtype=np.float64))
 
 
