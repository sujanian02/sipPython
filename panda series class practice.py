# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""
pip install pydataset
import pandas as pd
import numpy as np
from pydataset import data
df=data('mtcars')
df
df.shape[0]
pd.set_option('display.max_column',11)
df.dtypes
df.describe()
df.mpg.describe()
col1={'cyl','vs','am','gear','carb'}
df['col1']= data['col1'].astype('category') 
print(dir(pd),end=',')
len(dir(pd))
pd.read_csv?
print(dir(np),end=',')
len(dir(np))
#create pandas sereies
np1=np.array([10,4,5,6,7])
np1
np1.index#error
np1[0:3]
ps1=pd.Series([1,2,3,4,56,6])
ps1
#the data comes in a single column
ps1[0:3]
ps1.index#works here
ps2=pd.Series([1,4,2,5,6],index=['bba','ram','phd','a','ulas'],dtype='float32')
ps2
#here we defined the index and the dtype accordingly
ps2.index
ps2['bba']
ps2[['bba','ram','a']]
ps2['bba':'ulas']
ps2[0:5:2]
ps2.index.names
ps2.index.get_level_values#only one index here
ps2.sample(2)#any 2 rows
#%%%
#pandas _read/write to clipboard
dfread=pd.read_clipboard()
dfread
dfread[2:4].to_clipboard()
