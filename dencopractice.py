# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import pandas as pd
import numpy as np
pd.set_option('display.max_columns',15)
df=pd.read_csv('data/denco.csv')
df.head()
df.columns
df.dtypes
df.abs
df.describe()
df.shape
len(df)
df['region']=df['region'].astype('category')
df.dtypes
df.region.value_counts()
pd.set_option('display.max_rows',200)
df.partnum.value_counts().head(200)
df.region.value_counts()
df.region.value_counts().plot(kind='bar')
df.columns
pd.set_option('display.max_rows',15)
df.custname.value_counts()
df.custname.value_counts().sort_values(ascending=False)
df.groupby('custname').size()
df.sort_values(['custname'])
df.columns
df.groupby('custname').size().sort_values(ascending=False).head(5)
df.groupby('custname').size().sort_values(ascending=False).head(5)
df.groupby(['custname'])['margin'].nlargest(3)
df.sort_values(['revenue'],ascending=True).groupby('region').mean()
