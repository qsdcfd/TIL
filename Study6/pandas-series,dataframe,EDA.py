#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install pandas')


# In[2]:


import pandas as pd
ser = pd.Series(['a','b','c',3])
ser


# In[3]:


ser.values


# In[4]:


ser.index


# In[8]:


Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
ser3 = pd.Series(Country_PhoneNumber)
ser3


# In[10]:


ser3['Korea']


# In[9]:


ser3['Italy':]


# In[11]:


ser3.name = 'Country_PhoneNumber'
ser3.index.name = 'Country_Name'
ser3


# In[12]:


data = {'Region' : ['Korea', 'America', 'Chaina', 'Canada', 'Italy'],
        'Sales' : [300, 200, 500, 150, 50],
        'Amount' : [90, 80, 100, 30, 10],
        'Employee' : [20, 10, 30, 5, 3]
        }
s = pd.Series(data)
s


# In[13]:


s = pd.DataFrame(data)
s


# In[15]:


get_ipython().system(' mkdir -p ~/aiffel/data_represent/data')
get_ipython().system(' ln -s ~/data/covid19_italy_region.csv  ~/aiffel/data_represent/data')


# In[16]:


import pandas as pd
import os

csv_path = os.getenv("HOME") + "/aiffel/data_represent/data/covid19_italy_region.csv"
data = pd.read_csv(csv_path)
type(data)


# In[17]:


data


# In[18]:


data.head()


# In[19]:


data.tail()


# In[20]:


data.columns


# In[22]:


data.info()


# In[21]:


data.describe()


# In[23]:


data.isnull().sum()


# In[26]:


data['Country'].value_counts()


# In[25]:


data['RegionName'].value_counts().sum()


# In[27]:


print(data['TotalPositiveCases'].sum())
print(data['TestsPerformed'].sum())
print(data['Deaths'].sum())
print(data['Recovered'].sum())


# In[28]:


print(data['TestsPerformed'].corr(data['TotalPositiveCases']))
print(data['TestsPerformed'].corr(data['Deaths']))
print(data['TotalPositiveCases'].corr(data['Deaths']))

data.corr()


# In[30]:


data.drop(['Latitude','Longitude','Country','Date','HospitalizedPatients',  'IntensiveCarePatients', 'TotalHospitalizedPatients','HomeConfinement','RegionCode','SNo'], axis=1, inplace=True)

data.corr()


# In[ ]:




