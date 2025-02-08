# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 16:54:06 2025

@author: ASUS
"""

from scipy import linalg 
import numpy as np 

#define square matrix 
two_d_array = np.array([[4,5], [3,2]]) 

#pass values to det() function 
linalg.det(two_d_array) 

# Import math Library 
import math 
# Round a number upward to its nearest integer 
print(math.ceil(1.4)) 
print(math.ceil(5.3)) 
print(math.ceil(-5.3)) 
print(math.ceil(22.6)) 
print(math.ceil(10.0)) 

print(math.factorial(9)) 
print(math.factorial(6)) 
print(math.factorial(12)) 

print(math.floor(0.6)) 
print(math.floor(1.4)) 
print(math.floor(5.3)) 
print(math.floor(-5.3)) 
print(math.floor(22.6)) 
print(math.floor(10.0)) 

print (math.gcd(3, 6)) 
print (math.gcd(6, 12)) 
print (math.gcd(12, 36)) 
print (math.gcd(-12, -36)) 
print (math.gcd(5, 12)) 
print (math.gcd(10, 0)) 
print (math.gcd(0, 34)) 
print (math.gcd(0, 0)) 

# Print the square root of different numbers 
print (math.sqrt(10)) 
print (math.sqrt (12)) 
print (math.sqrt (68)) 
print (math.sqrt (100)) 
# Round square root downward to the nearest integer 
print (math.isqrt(10)) 
print (math.isqrt (12)) 
print (math.isqrt (68)) 
print (math.isqrt (100)) 


#Check whether some values are NaN or not 
print (math.isnan (56)) 
print (math.isnan (-45.34)) 
print (math.isnan (+45.34)) 
print (math.isnan (math.inf)) 
print (math.isnan (float("nan"))) 
print (math.isnan (float("inf"))) 
print (math.isnan (float("-inf"))) 
print (math.isnan (math.nan)) 

#define two dimensional array 
arr= np.array([[5,4], [6,3]])

 #pass value into function 
eg_val, eg_vect= linalg.eig(arr)

 #get eigenvalues 
print(eg_val) #get eigenvectors print(eg_vect) 
