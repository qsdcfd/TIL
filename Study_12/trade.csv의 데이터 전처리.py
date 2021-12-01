#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("👽 Hello.")


# In[5]:


import os

csv_file_path = os.getenv('HOME')+'/aiffel/data_preprocess/data/trade.csv'
trade = pd.read_csv(csv_file_path) 
trade.head()


# In[6]:


print('전체 데이터 건수:', len(trade))


# In[7]:


print('컬럼별 결측치 개수')
len(trade) - trade.count()


# In[8]:


trade = trade.drop('기타사항', axis=1)
trade.head()


# In[9]:


trade.isnull()


# In[10]:


trade.isnull().any(axis=1)


# In[11]:


trade[trade.isnull().any(axis=1)]


# In[12]:


trade.dropna(how='all', subset=['수출건수', '수출금액', '수입건수', '수입금액', '무역수지'], inplace=True)
print("👽 It's okay, no biggie.")


# In[13]:


trade[trade.isnull().any(axis=1)]


# In[14]:


trade.loc[[188, 191, 194]]


# In[15]:


trade.loc[191, '수출금액'] = (trade.loc[188, '수출금액'] + trade.loc[194, '수출금액'] )/2
trade.loc[[191]]


# In[16]:


trade.loc[191, '무역수지'] = trade.loc[191, '수출금액'] - trade.loc[191, '수입금액'] 
trade.loc[[191]]


# In[17]:


#-- 아래에 코드를 작성해 주세요. --#
trade.loc[191,'수출금액']=trade.loc[188,'수출금액']
trade.loc[[191]]


# In[18]:


trade.duplicated()


# In[19]:


trade[trade.duplicated()]


# In[20]:


trade[(trade['기간']=='2020년 03월')&(trade['국가명']=='중국')]


# In[21]:


trade.drop_duplicates(inplace=True)
print("👽 It's okay, no biggie.")


# In[24]:


def outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index
print("👽 It's okay, no biggie.")


# In[25]:


trade.loc[outlier(trade, '무역수지', 1.5)]


# In[26]:


trade.loc[outlier(trade, '무역수지', 2)]


# In[27]:


trade.loc[outlier(trade, '무역수지', 3)]


# In[28]:


def not_outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col]) <= z].index
print("👽 It's okay, no biggie.")


# In[29]:


trade.loc[not_outlier(trade, '무역수지', 1.5)]


# In[30]:


def outlier2(df, col):
    q1 = df[col].quantile(0.32)
    q3 = df[col].quantile(0.56)
    iqr = q3 - q1
    return df[(df[col] < q1-1.5*iqr)|(df[col] > q3+1.5*iqr)]

outlier2(trade, '무역수지')


# In[31]:


# 정규분포를 따라 랜덤하게 데이터 x를 생성합니다. 
np.random.seed(2020)
x = pd.DataFrame({'A': np.random.randn(100)*4+4,
                 'B': np.random.randn(100)-1})
x


# In[32]:


# 데이터 x를 Standardization 기법으로 정규화합니다. 
x_standardization = (x - x.mean())/x.std()
x_standardization


# In[33]:


# 데이터 x를 min-max scaling 기법으로 정규화합니다. 
x_min_max = (x-x.min())/(x.max()-x.min())
x_min_max


# In[34]:


fig, axs = plt.subplots(1,2, figsize=(12, 4),
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


# In[35]:


fig, axs = plt.subplots(1,2, figsize=(12, 4),
                        gridspec_kw={'width_ratios': [2, 1]})

axs[0].scatter(x['A'], x['B'])
axs[0].set_xlim(-5, 15)
axs[0].set_ylim(-5, 5)
axs[0].axvline(c='grey', lw=1)
axs[0].axhline(c='grey', lw=1)
axs[0].set_title('Original Data')

axs[1].scatter(x_min_max['A'], x_min_max['B'])
axs[1].set_xlim(-5, 5)
axs[1].set_ylim(-5, 5)
axs[1].axvline(c='grey', lw=1)
axs[1].axhline(c='grey', lw=1)
axs[1].set_title('Data after min-max scaling')

plt.show()


# In[36]:


# trade 데이터를 Standardization 기법으로 정규화합니다. 
cols = ['수출건수', '수출금액', '수입건수', '수입금액', '무역수지']
trade_Standardization= (trade[cols]-trade[cols].mean())/trade[cols].std()
trade_Standardization.head()


# In[37]:


trade_Standardization.describe()


# In[38]:


# trade 데이터를 min-max scaling 기법으로 정규화합니다. 
trade[cols] = (trade[cols]-trade[cols].min())/(trade[cols].max()-trade[cols].min())
trade.head()


# In[44]:


#trade 데이터의 국가명 컬럼 원본
print(trade['국가명'].head())  

# get_dummies를 통해 국가명 원-핫 인코딩
country = pd.get_dummies(trade['국가명'])
country.head()


# In[45]:


trade = pd.concat([trade, country], axis=1)
trade.head()


# In[46]:


trade.drop(['국가명'], axis=1, inplace=True)
trade.head()


# In[ ]:




