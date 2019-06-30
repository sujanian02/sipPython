# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""
#multi indexing
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pydataset import data
data('iris')
data('titanic')
data
mtcars=data('mtcars')
mtcars.head()
data1=mtcars
data1.columns#column names
data1.values#values of Df(data frame)
data1.index
data1.dtypes#the difference between float(32 and 64)64 take more data ,so we  can take large values storred in it
data1[['am','vs','cyl','gear','carb']]=data1[['am','vs','cyl','gear','carb']].astype('category')
data1.dtypes
data1.iloc[0:3,0:4]
#now we will change the default index to a column
data2=data1.reset_index()
data2.iloc[0:3,0:4]
data2.columns
data2.rename({'index':'car_name'},inplace=True,axis=1)
#old to new name #axis can be 'column" or 1 here other wise 0 and 'rows' as well
data2.head()
data3cyl=data2.set_index('cyl')#implace not done because just want to see and  not change permannetly
data3cyl
#index column is shifted a bit down
data3cyl.loc[6]
data2.dtypes
data3gear=data3cyl.reset_index().set_index('gear').head()
data3gear
data3am=data3gear.reset_index().set_index('am').head()
data3am
data3am.set_index('cyl',append=True).set_index('vs',append=True)#multi level indexingis done by append
#%%
data2.columns
data2.head()
dataGg=data2.groupby('gear')['mpg'].mean()#gearwise mean milege
dataGg.head()
type(dataGg)
dataGg[2]
dataGga=data2.groupby(['gear','am']).mpg.mean()
dataGga
dataGga.index
#unstack function will make one index a row and one column and happens only for multiple index only and not for single single indexing
dataGga.unstack()#works for this 
dataGg.unstack()#doesnt work for it As it m=doesnt have multiple index
dataGgcc=data2.groupby(['gear','carb','cyl']).mpg.mean()
dataGgcc.head()
dataGgcc.loc[3]#will locate the numbe in the first column(here in gear)
dataGgcc.unstack()
dataGgcc.loc[3,1]#will take the value from 1st and 2nd index
dataGgcc.loc[3,4,8]#will take the value from 1st 2nd and 3rd index
dataGgcc.sort_index()
dataGgcc.sort_index(level=1)#will sort according to the second level
dataGgcc.sort_index(level=2)#now in level 3
dataGgcc.sort_index(level=[0,1])#will sort 1st the o level and then level 1
mtcars.sort_values(['gear','mpg']).head()
mtcars.sort_values(['mpg','am','wt'],ascending=[True,False,True]).head(10)#giving ascending descending and ascning vallues
mtcars[['mpg','am','wt']].sort_values(['mpg','am','wt'],ascending=[True,False,True]).head(10)
mtcars.iloc[mtcars['mpg']>25,1:5]
mtcars.loc[(mtcars['mpg']>25)&(mtcars['hp']>35),['mpg','hp']]
mtcars.loc[(mtcars['vs']==1)|(mtcars['am']==1),['mpg','hp','vs','am']]
#pivot table
mtcars.pivot_table(index=['gear'],columns=['vs','am'],aggfunc={'mpg':np.mean,'wt':min})
mtcars.pivot_table(index=['gear','vs'],values='mpg',columns='am')
mtcars.pivot_table(index='gear',values="mpg",columns='am')
