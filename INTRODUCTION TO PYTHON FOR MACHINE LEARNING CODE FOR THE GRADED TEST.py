#!/usr/bin/env python
# coding: utf-8

# In[13]:


#importing the datasets
import numpy as np
import pandas as pd 


# In[14]:


A = [1,2,3,4,5,6]
B= [13,21,34]
A_B = A + B
#A_B is the concatination of A and B
A_B


# In[15]:


data = pd.read_csv ('fuel_ferc1.csv')
data.head()


# In[16]:


np.identity(3)


# In[17]:


data.groupby('fuel_type_code_pudl')['fuel_cost_per_unit_burned'].mean()


# In[25]:


data.describe()
#to show the descriotive details of the data


# In[19]:


data.skew()


# In[20]:


data.kurt()


# In[21]:


data.info()


# In[22]:


data.isnull().sum()


# In[23]:


data.corr()


# In[24]:


data.groupby('report_year')['fuel_cost_per_unit_delivered'].mean()


# In[ ]:




