#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("👽 Hello.")


# In[6]:


import os

csv_file_path = os.getenv('HOME')+'/aiffel/data_preprocess/data/vgsales.csv'
vgsales = pd.read_csv(csv_file_path) 
vgsales.head()


# In[7]:


print('전체 데이터 건수:', len(vgsales))


# In[8]:


print('컬럼별 결측치 개수')
len(vgsales) - vgsales.count()


# In[10]:


vgsales.isnull()


# In[11]:


vgsales.isnull().any(axis=1)


# In[12]:


vgsales[vgsales.isnull().any(axis=1)]


# In[13]:


trade.dropna(how='all', subset=['Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales'], inplace=True)
print("👽 It's okay, no biggie.")


# In[18]:


vgsales[vgsales.isnull().any(axis=1)]


# In[19]:


vgsales.loc[[16427, 16494, 16543]]


# In[20]:


vgsales.loc[16427,'Year']=vgsales.loc[16494,'Year']
vgsales.loc[[16427]]


# In[21]:


vgsales.duplicated()


# In[26]:


vgsales[vgsales.duplicated()]


# In[25]:


vgsales[(vgsales['Year']=='2011.0')&(vgsales['Name']=='Driving Simulator 2011')]


# In[27]:


vgsales.drop_duplicates(inplace=True)
print("👽 It's okay, no biggie.")


# In[28]:


def outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index
print("👽 It's okay, no biggie.")


# In[32]:


vgsales.loc[outlier(vgsales, 'Global_Sales', 1.5)]


# In[33]:


vgsales.loc[outlier(vgsales, 'Global_Sales', 2)]


# In[34]:


vgsales.loc[outlier(vgsales, 'Global_Sales', 3)]


# In[35]:


def not_outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col]) <= z].index
print("👽 It's okay, no biggie.")


# In[36]:


trade.loc[not_outlier(trade, 'Global_Sales', 1.5)]


# In[37]:


def outlier2(df, col):
    q1 = df[col].quantile(0.32)
    q3 = df[col].quantile(0.56)
    iqr = q3 - q1
    return df[(df[col] < q1-1.5*iqr)|(df[col] > q3+1.5*iqr)]

outlier2(vgsales, 'Global_Sales')


# In[39]:


np.random.seed(2010)
x = pd.DataFrame({'A': np.random.randn(100)*4+4,
                 'B': np.random.randn(100)-1})
x


# In[40]:


x_standardization = (x - x.mean())/x.std()
x_standardization


# In[41]:


x_standardization = (x - x.mean())/x.std()
x_standardization


# In[44]:


fig, axs = plt.subplots(1,2, figsize=(12, 8),
                        gridspec_kw={'width_ratios': [2, 1]})

axs[0].scatter(x['A'], x['B'])
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-5, 5)
axs[0].axvline(c='grey', lw=1)
axs[0].axhline(c='grey', lw=1)
axs[0].set_title('Original Data')

axs[1].scatter(x_standardization['A'], x_standardization['B'])
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].axvline(c='grey', lw=1)
axs[1].axhline(c='grey', lw=1)
axs[1].set_title('Data after standardization')

plt.show()


# In[49]:


fig, axs = plt.subplots(1,2, figsize=(12, 6),
                        gridspec_kw={'width_ratios': [2, 1]})

axs[0].scatter(x['A'], x['B'])
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-5, 5)
axs[0].axvline(c='grey', lw=1)
axs[0].axhline(c='grey', lw=1)
axs[0].set_title('Original Data')

axs[1].scatter(x_standardization['A'], x_standardization['B'])
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].axvline(c='grey', lw=1)
axs[1].axhline(c='grey', lw=1)
axs[1].set_title('Data after standardization')

plt.show()


# In[51]:


cols = ['Platform','Year','Genre','Publisher','NA_Sales','EU_Sales','JP_Sales','Other_Sales','Global_Sales']
vgsales_Standardization= (vgsales[cols]-vgsales[cols].mean())/vgsales[cols].std()
vgsales_Standardization.head()


# In[52]:


vgsales_Standardization.describe()


# In[54]:


print(vgsales['Name'].head())  

# get_dummies를 통해 국가명 원-핫 인코딩
country = pd.get_dummies(vgsales['Name'])
country.head()


# In[60]:


vgsales.drop(['Name'], axis=1, inplace=True)
vgsales.head()


# In[ ]:




