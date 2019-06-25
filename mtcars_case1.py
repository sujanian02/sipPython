# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""
import statsmodels.api as sm
dataset_mtcars = sm.datasets.get_rdataset(dataname='mtcars', package='datasets')
dataset_mtcars.data.head()
mtcars=dataset_mtcars.data
#structure
mtcars.dtypes
#summary
mtcars.describe
#print first/last few rows
mtcars.head()
mtcars.tail()
#print no. of rows
mtcars.shape[0]
#print no. of columns
mtcars.shape[1]
#print names of columns
mtcars.columns
#filter rows
#cars with cyl 8
mtcars[mtcars.cyl==8]
#cars  with mpg<=27
mtcars[mtcars.mpg<=27]
#rows match auto tx

#first row
mtcars.head(1)
#last row
mtcars.tail(1)
# 1st, 4th, 7th, 25th row + 1st 6th 7th columns.
mtcars.iloc[[1,4,7,25],[1,6,7]]
# first 5 rows and 5th, 6th, 7th columns of data frame
mtcars.iloc[[1,2,3,4,5],[5,6,7]]
#rows between 25 and 3rd last
mtcars.iloc[[25,26,27,28,29],:]
#alternative rows and alternative column

#find row with Mazda RX4 Wag and columns cyl, am
mtcars.loc[['Mazda RX4 Wag'],['cyl','am']]

#find row betwee Merc 280 and Volvo 142E Mazda RX4 Wag and columns cyl, am
mtcars.loc[['Merc 280', 'Volvo 142E'], ['cyl']]


# mpg > 23 or wt < 2
[mtcars[mtcars.mpg > 23], mtcars[mtcars.wt < 2]]
#using lambda for above


#with or condition
#find unique rows of cyl, am, gear

mtcars.cyl.unique(), mtcars.am.unique(), mtcars.gear.unique()


#create new columns: first make a copy of mtcars to mtcars2
mtcars2 = mtcars
mtcars2

mtcars2['newdisp'] = mtcars['disp'] / 61 
mtcars2.head()


# multiple mpg * 1.5 and save as original column
mtcars2.mpg*1.5
mtcars2['mpg']=mtcars2.mpg*1.5
mtcars2.head()