# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import pandas as pd
import numpy as np
chipo=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/chipotle.tsv',sep= '\t')
chipo.head(11)
chipo.shape[0]
chipo.info()
chipo.shape[1]
chipo.columns
chipo.index
chipo.groupby('item_name')['quantity'].sum().sort_values(ascending=False).head()
pd.set_option('display.max_columns',5)
chipo.columns
chipo.groupby('choice_description')['quantity'].sum().sort_values(ascending=False).head(1)
chipo.quantity.sum()
chipo.dtypes
