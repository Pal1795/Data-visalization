
# coding: utf-8

# In[215]:


import pandas as pd
df = pd.read_csv("milk_production.csv")
df.head()


# In[88]:


milk = df[["State/ UT Name","Cow Milk-2013-14","Boffalo Milk-2013-14","Goat Milk-2013-14"]]


# In[170]:


#max_cow = milk[milk["State/ UT Name"] == milk.max()]
import numpy as np
#add = df[df["State/ UT Name"],[df["Cow Milk-2013-14"] + df["Boffalo Milk-2013-14"] + df["Goat Milk-2013-14"]]]
#add
#add = add.max()  
#print(add)
#add[add==add.max()]
#add=df['State/ UT Name']
#df[df["State/ UT Name"]==add.max()]
#milk[milk["State/ UT Name"]==add.max()]
maxx=df["Cow Milk-2013-14"] + df["Boffalo Milk-2013-14"] + df["Goat Milk-2013-14"]
#df.head()
#df["ajith"].max()
#df[df["State/ UT Name"]==df["ajith"].max()]
#df.head(2)
#maxx.max()
#a=np.where(maxx==maxx.max())
#new=df.iloc[a]
#new
#print(df)
df[df["ajith"]==df["ajith"].max()]["State/ UT Name"]


# In[23]:


max_cow


# In[109]:


df.head(5)


# In[172]:


df["y2011"] =(df["Cow Milk-2010-11"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]).sort_values(ascending=False)
df["y2012"]= df["Cow Milk-2011-12"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]
df["y2014"]= df["Cow Milk-2013-14"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]
df["y2015"]= df["Cow Milk-2014-15"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]
#y2011.head()
#y2011.sort_values(ascending = False).head()
#y2015= df["Cow Milk-2010-11"] + df["Boffalo Milk-2010-11"] + df["Goat Milk-2010-11"]
print(df.sort_values('y2011',ascending=False)["State/ UT Name"].head())
df.sort_values('y2012',ascending=False)["State/ UT Name"].head()
#print(df.head())
#np.where(df["State/ UT Name"] == df["y2011"].sort_values(ascending=False))
#df[df["State/ UT Name"]df["y2011"].sort_values(ascending=False)]


# In[122]:


df[["State/ UT Name","Cow Milk-2010-11"]]


# In[179]:


#df[df["Cow Milk-2010-11"].mean() and df["State/ UT Name"]=="Rajasthan"]
df.head(2)


# In[180]:


df["cow_allyear"]=df["Cow Milk-2010-11"]+df["Cow Milk-2011-12"]+df["Cow Milk-2013-14"]+df["Cow Milk-2014-15"]+df["Cow Milk-2015-16"]


# In[182]:


df[df["cow_allyear"].mean() and df["State/ UT Name"]=="Uttar Pradesh"]


# In[185]:


df.head(2)


# In[184]:


df["y2016"]= df["Cow Milk-2015-16"] + df["Boffalo Milk-2015-16"] + df["Goat Milk-2015-16"]


# In[208]:


df[df["y2016"].ge(df["y2015"]) & df["y2015"].ge(df["y2014"])].head()


# In[210]:


pro = pd.read_csv("products.csv")
pro


# In[212]:


pro["Product"].unique()


# In[214]:


pro["Retailer country"].unique()

