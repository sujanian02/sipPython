# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

import pandas as pd
import numpy as np
users=pd.read_csv('https://raw.githubusercontent.com/justmarkham/DAT8/master/data/u.user',sep='|')
users.set_index('user_id',inplace=True)
users.head()
users.shape[0]
users.shape[1]
users.columns
users.occupation
users.index
users.dtypes
users.occupation.value_counts().count()
users.groupby('occupation').size().sort_values(ascending=False).head(1)
users.describe()
users.describe(include='all')
users.occupation.describe()
users.dtypes
users.age.mean()
users.age.min()
users.age.value_counts().sort_values(ascending=True).head()
