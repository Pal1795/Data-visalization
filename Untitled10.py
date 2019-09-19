
# coding: utf-8

# In[5]:

import numpy as np
import pandas as pd
from pandas import DataFrame


# In[9]:

df=pd.read_csv("central-India_rainfall_act_dep_1901_2016.csv")
df


# In[18]:

df1=pd.read_csv("south_pen-India_rainfall_act_dep_1901_2016.csv")
df1


# In[33]:

df2=pd.read_csv("ne-India_rainfall_act_dep_1901_2016.csv")
df2


# In[23]:

df3=pd.read_csv("nw-India_rainfall_act_dep_1901_2016.csv")
df3


# In[35]:

df1["Actual Rainfall: JUN"].max()


# In[86]:

df1[df1['Actual Rainfall: JUN']==df1['Actual Rainfall: JUN'].max()] [['YEAR','Actual Rainfall: JUN']]


# In[85]:

df2[df2['Actual Rainfall: JUN']==df2['Actual Rainfall: JUN'].max()] [['YEAR','Actual Rainfall: JUN']]


# In[81]:

df[df['Actual Rainfall: JUN']==df['Actual Rainfall: JUN'].min()] [["YEAR"]] #CENTRAL INDIA


# In[78]:

df1[df1['Actual Rainfall: JUN']==df1['Actual Rainfall: JUN'].min()] [["YEAR"]] #south india


# In[79]:

df2[df2['Actual Rainfall: JUN']==df2['Actual Rainfall: JUN'].min()] [["YEAR"]] #north east


# In[80]:

df3[df3['Actual Rainfall: JUN']==df3['Actual Rainfall: JUN'].min()] [["YEAR"]] #north west


# In[54]:

import pandas as pd
df4=pd.read_excel("MONTHLY_ACTUAL_RAINFALL_FROM_2009_TO_2011.XLS")
df4


# In[55]:

import pandas as pd
df5=pd.read_excel("METEOROLOGICAL_SUB_DIVISION_WISE_ANNUAL_RAINFALL.xls")
df5


# In[82]:

df5[df5['Sub-division']==df5['Sub-division'].min()][['2010 (in millimetre)','Sub-division']]


# In[83]:

import matplotlib.pyplot as plt
plt.plot(df5['Sub-division'],df5['2002 (in millimetre)'],linestyle="dashed",marker='*',color="purple")
x_pos=np.arange(len(df5))
plt.Xlabel("Sub divisions")
plt.ylabel("Rainfall")
plt.legend()
plt.title('rainfall analysis')
plt.show()


# In[69]:

import matpltlib.pyplot as plt
rc('font', weight='bold')



# In[ ]:



