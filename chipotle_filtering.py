# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import pandas as pd
import numpy as np
chipo=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep='\t')
# clean the item_price column and transform it in a float
chipo.dtypes
price=[float(value[1:-1])for value in chipo.item_price]
chipo.item_price=price

# reassign the column with the cleaned prices
price=[float(value[1:-1]) for value in chipo.item_price]
chipo.item_price=price
# delete the duplicates in item_name and quantity
chipo_filtered=chipo.drop_duplicates(['item_name','quantity'])
# select only the products with quantity equals to 1
chipo.quantity[chipo.quantity==1]
chipo.dtypes
chipot=chipo[["item_name","item_price"]]
chipot.sort_values(by='item_name')
chipo.dtypes
chipo[['item_price','quantity']].sort_values(by='item_price',ascending=False).head(1)
chipo.item_name.iloc[3598]
chipo[chipo.item_name=='Veggie Salad Bowl'].count()
chipo[(chipo.item_name=='Canned Soda')&(chipo.quantity>1)].count()
