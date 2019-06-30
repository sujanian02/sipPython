# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""
#simply copuying things from excel to python
import pandas pd
dfread=pd.read_clipboard()
dfread
pd.set_option('display.max_columns',9)
dfread[2:3].to_clipboard()
dfread.iloc[4,7]
dfread.iloc[1:9,0:7]
dfread.iloc[2:11,0:8]
dfread.loc[1:9,['State','date']]

