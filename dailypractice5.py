# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import numpy as np
np1=np.arange(1,10)
np1
type(np1)
np2=np.array([90,50,40,96])
np2
np.sort(np2)
np3=np.array([[1,4,3],[4,6,7],[9,40,45]])
np3
np3.shape
import pandas as pd
pd?
df1=pd.DataFrame({'rollno.':[1,2,3,4,5],'name':['mayank','rajesh','lala','keshav','dinesh'],'marks':[21,23,34,43,55],'sex':['m','f','m','f','m']})
df1
rollno=[1,2,3,4,5]
name=['mayank','rajesh','bhagat','lala','dharmendr']
marks=[45,56,48,78,49]
sex=['m','f','m','f','m']
mapped=zip(rollno,name,marks,sex)
wape=set(mapped)
wape
df1.columns
df1.describe()
df1.dtypes
df1.shape
df1.groupby('sex').size()
df1.groupby('sex')['marks'].mean().max()
df1.groupby('sex').aggregate({'marks':[np.mean,'max']})
df1.groupby('sex').aggregate({'marks':[np.mean,'max']})
import matplotlib.pyplot as plt
df1.groupby('sex').size().plot(kind='bar')
import seaborn as sns
iris=sns.load_dataset('iris')
sns.pairplot(iris)
import statsmodels.api as sm
mtcars=sm.datasets.get_rdataset(dataname='mtcars',package='datasets')
mtcars.data.head()
#sets
set1={1,2,'ram','raghu',True}
set1
set1[0]
set1
for i in set1:
	print(i,end=' ')
'ram' in set1	
'raja' in set1
set1.add('Pooja')
set1
set1.add('Pooja')
set1
set1.update(['radhe','lala'])
set1
set1.update('bhagu')
set1
len(set1)
set1.remove('Pooja')
set1
set1.remove('Akhil')
set1.discard('Akhil')
set1
set1.discard('lala')
set1
set1.pop()
set1
