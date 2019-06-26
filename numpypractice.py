# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import numpy as np
np.arange(10)
np.arange(0,10)
x=np.arange(10,21)
x
x[9]
x[0],x[5],x[2]
x[-1]
x[0:5]
x[0:8:2]
x[10:0:-1]
x[0::2]
np.random.random(size=10)
np.random.randint(10,size=6)
np.random.randint(100,size=12)
np.random.randint(10,size=(3,4))
np.random.randint(20,size=(3,3,3))
x2=np.random.randint(10,size=(3,4))
x2
np.random.randint(60,99,size=(100))
np.ptp(x2)
np.min(x2)
np.max(x2)
np.std(x2)
np.mean(x2)
np.median(x2)
x2[1,1]
x2[1,1]
x2[:2,]
x2[:3,]
x2[:,:1]
x2[:2,:3]
x2[::2,::3]
x2[::-1,::-1]
x3=np.random.randint(10,size=(3,4,5))
x3
np.ndim(x3)
np.shape(x3)
np.size(x3)
np.random.randint(1,10,size=10)
xn1=np.random.normal(0,1,100)
xn1
np.mean(xn1)
np.std(xn1)
xn2=np.random.normal(0,1,100000000)
xn2
np.mean(xn2)
np.std(xn2)
#larger the values ,larger will be the accuracy if the data of std and mean
len(xn1),xn1.mean(),xn1.std()
len(xn2),xn2.mean(),xn2.std()
import seaborn as sns
sns.kdeplot(xn1)
sns.kdeplot(xn2)
np.linspace(0,10,5)
np.linspace(10,15,9)
q=np.linspace(11,12,10)
q
np.round(q,2)
np.floor([1.2,1.6])
np.ceil([1.2,1.7])
np.trunc([1.3222,1.568])
np.round([1.3443,1.345677],2)
#floor and trunc gives a different value for negative values
xe=np.empty(10)
xe#use with caution
np.eye(4)
np.zeros([10])
np.zeros(shape=(3,4))
np.ones(shape=(3,5))
np.ones([10])
np.full((3,4),[5])
np.full((5,5),[3.14])
s=np.full((7,7),[np.pi])
s
np.round(s)
np.full((5,4),['mickey'])
np.array([1,2,3,4,5,6]).reshape(2,3)
ns1=np.array([1,2,3,4])
ns1.shape,ns1.size
w=[1,2,3,4,5,6,78,9,12,0,]
w
np.array(w).reshape(2,5)
np.concatenate([w,np.zeros(2)]).reshape(6,2)
e=np.arange(1,40)
e
x=np.arange(6).reshape(2,3)
x
y=np.arange(10,16).reshape(2,3)
y
np.concatenate([x,y],axis=0)
np.concatenate([x,y],axis=1)
np.vstack([x,y])
np.hstack([x,y])
x=np.arange(10,19)
x
x1,x2,x3=np.split(x,[3,5])
x1,x2,x3
y=x.reshape([3,3])
y
x1,x2,x3=np.split(x,[3,2])
x1,x2,x3
y=x.reshape([3,3])
y
upper,lower=np.vsplit(y,[2])
upper
lower
left,right=np.hsplit(y,[1])
left
right
np.arange(1,13).reshape(3,4,order='C')
np.arange(1,13).reshape(3,4,order='F')
np.arange(1,13).reshape(3,4,order='F').T
np.arange(1,13).reshape(3,4)
x=np.arange(5)
x
x+5
np.add(x,5)
np.multiply(x,10)
y=np.empty(5)
y=np.zeros(5)
y
np.multiply(x,5,out=y)
x=np.random.randint(30,500,size=20000)
x
x.sum(axis=0)
x.mean(axis=0)
x.sum(axis=1)
np.median(x)  #median values in full dataset
np.max(x)  #max
max(x)  #will not work, as it is multi
max([1,2,3])  #this will work
np.min(x) #min
np.equal(x, 49) #all values equal to 48
np.greater(x, 40) #values greater than 40
np.sum(np.greater(x,40))  #how many values > 40
sum(np.greater(x,40))
np.less(x, 50)  #values < 50
np.greater_equal(x, 40)  #values >= 40
x < 40 #another way T/ F
np.sum(x < 40)  #how many values < 40
x
np.sum(x < 40, axis=0)  #in each col, values < 40

x=np.random.randint(10, size=(3,4))
x
np.all(x > 4)
np.any(x > 4)
np.sum(x > 1)
np.sum(x > 3, axis=1)
np.sum(x > 3, axis=0)
np.sum( (x> 3) & (x < 7), axis=0)
np.sum( ~((x> 3) & (x < 7)), axis=0)


#sort
#%%
x = np.random.randint(100,size=50)
x
np.sort(x)
np.argsort(x)

x = np.random.randint(10,size=10)
x
np.partition(x, 3)  #sort
np.partition(x, 4)  #sort
array = np.array([7, 5, 3, 2, 6, 1, 4])
array
# Sort in ascending order
sorted_array = np.sort(array)
# [1, 2, 3, 4, 5, 6, 7]

# Reverse the sorted array
reverse_array = sorted_array[::-1]
reverse_array
# [7, 6, 5, 4, 3, 2, 1]