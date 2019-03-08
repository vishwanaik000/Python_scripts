# -*- coding: utf-8 -*-
"""
Created on Tue Aug 28 17:37:18 2018

@author: 28587
"""
import numpy as np

a1 = np.array([1,2,3,4,5])

print(a1)
type(a1)

a2 = np.array([[1,2,3,4,5,6], [1,2,6,4,8,9]])
a3 = np.array([[11,22,23,34,15,26], [11,23,62,41,82,19]])

a3.shape
a2.reshape(6,2)
a2.transpose()
print( a2)
print( a3)
a4 = a2 + a3
print( a4)
a5 = a2.dot(a3.reshape(6,2))
print( a5)

#converting array value to sin value
a6 = np.sin(a5)
print( a6)

#converting array value to cos value
a7 = np.cos(a5)
print( a7)

#sin^2 + cos^2 = 1
a8 = a6**2 + a7**2
print( a8)

#padding zeroes
np1 = np.zeros(10) #array of 10 zeros. here all zeros are of float type.
print( np1)
np2 = np.zeros(10,dtype = int) #array of 10 zeros. here all zeros are of int type.
print( np2)
np3 = np.zeros(10,dtype = int) #array of 10 one. here all one are of int type.
print( np3)
np4 = np.zeros((4,5),dtype = int) #array of 10 zeros. here its an array of (4,5)
print( np4)

#other operations
a1.sum()
a1.min()
a1.max()