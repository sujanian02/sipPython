# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import pandas as pd
import numpy as np
food=pd.read_csv('F:\pyWork\pyProjects\en.openfoodfacts.org.products.tsv',sep='\t')
food.head()
food.dtypes
food.shape[0]
food.shape[1]
food.columns
x=food.columns[104]
food['-glucose_100g'].dtype
food.index
food.loc[:,'product_name']
food.product_name.iloc[18]
