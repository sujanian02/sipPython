# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: %(mayankprashar)s
"""

#graph plots
import numpy as np
import matplotlib.pyplot as plt
x=np.linspace(0,10,100)
x
np.sin(x)
fig=plt.figure()
plt.axis([1,-1,2,13])
plt.plot(x,np.sin(x),color='red')
plt.show()
#%%%
x=np.arange(0,10)
x
y=x ^ 2
x,y
plt.xlim(2,6)
plt.ylim(2,8)
plt.title("graphic drawing")
plt.xlabel('time')
plt.ylabel('distance')
plt.plot(x,y)
plt.axis('tight')
plt.axis('equal')
#%%%
plt.plot(x,np.tan(x),label='X Curve')
plt.plot(x,np.cos(x),label='Y Curve')
plt.title('sine and cos curve')
plt.xlabel('mayank')
plt.ylabel('neeraj')
plt.axis('tight')
plt.legend()
#%%%
x=np.linspace(0,10,1000)
ax=plt.axes()
ax.plot(x,np.sin(x))
ax.set(xlim=(0,10),ylim=(-2,2),xlabel='lala',ylabel='raja',title='raja or lala bhai');
#%%%
import pandas as pd
df=pd.DataFrame(np.random.rand(10,5),columns=['A','B','C','D','E'])
df
df.plot.box(grid=True)
plt.boxplot(df.A,notch=True)
