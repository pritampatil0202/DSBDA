#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[4]:


import pandas as pd


# In[7]:


df=pd.read_csv("C:\\Users\\Welcome\\Downloads\\iris.csv")


# In[8]:


df


# In[9]:


df.min()


# In[10]:


df.max()


# In[11]:


df.mode()


# In[12]:


df.median()


# In[15]:


df


# In[16]:


df.std()


# In[17]:


df.loc[:,'Age'].mode()


# In[18]:


df.mean()


# In[19]:


df.loc[:,'petal_width'].mean()


# In[20]:


df.mean(axis=1)[0:4]


# In[21]:


df.loc[:,'petal_width'].median()


# In[22]:


df.loc[:,'petal_width'].min(skipna = False)


# In[ ]:




