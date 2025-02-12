# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 00:47:06 2025

@author: ASUS
"""

import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
S=pd.Series([11, 28, 72, 3, 5, 8]) 
print(S)

print(S.index)
print(S.values)
 
X=np.array([14, 28, 55, 90, 56, 89]) 
print(X) 
print(S.values) 

#both are the same type:     
print(type (S.values), type (X)) 

fruits= ['apples', 'oranges', 'cherries', 'pears']
S= pd.Series([20, 33, 52, 10], index=fruits)
S2= pd.Series([17, 13, 31, 32], index=fruits)
print(S+ S2)
print("sum of S: ", sum(S))

fruits= ['apples','oranges', 'cherries', 'pears'] 
quantities=[20, 33, 52, 10] 
S=pd.Series(quantities, index=fruits) 
S1=pd.Series(quantities, index=fruits) 
print(S+S1)

fruits= ['peaches', 'oranges', 'cherries', 'pears']
fruits2= ['raspberries', 'oranges', 'cherries', 'pears']
S= pd.Series([20, 33, 52, 10], index=fruits)
S2= pd.Series([17, 13, 31, 32], index=fruits2)
print(S+ S2)



fruits= ['apples', 'oranges', 'cherries', 'pears']
fruits_tr= ['elma', 'portakal', 'kiraz', 'armut']
S= pd.Series([20, 33, 52, 10], index=fruits)
S2= pd.Series([17, 13, 31, 32], index=fruits)
print(S+ S2)
print("sum of S: ", sum(S))


fruits= ['apples', 'oranges', 'cherries', 'pears']
fruits_tr= ['elma', 'portakal', 'kiraz', 'armut']
S= pd.Series([20, 33, 52, 10], index=fruits)
S2= pd.Series([17, 13, 31, 32], index=fruits_tr)
print(S+ S2)

print(S['apples'])


plt.plot([1,2,3,4], [1,4,9,16])


plt.title("First Flot")
plt.xlabel("X lable")
plt.xlabel("Y lable")
plt.figure(figsize=(15,5))

plt.show()


plt.plot([1,2,3,4], [1,4,9,16],"go")
plt.figure(figsize=(15,25))
plt.show()

