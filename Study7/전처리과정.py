#!/usr/bin/env python
# coding: utf-8

# 중복된 데이터를 찾아 제거할 수 있고, 결측치(missing data)를 제거하거나 채워 넣을 수 있다.
# 데이터를 정규화시킬 수 있다.
# 이상치(outlier)를 찾고, 이를 처리할 수 있다.
# 범주형 데이터를 원-핫 인코딩할 수 있다.
# 연속적인 데이터를 구간으로 나눠 범주형 데이터로 변환할 수 있다.
# 
# <배울 내용>
# 
# 결측치(Missing Data)
# [결측치 처리 방법]
# i) 결측치가 있는 데이터 제거
# ii)결측치를 어떤 값으로 대체(데이터마다 특성 반영하여 해결)
#  i-1)특정값 지정. 결측치가 많은 경우( 모두 같은 값 대체-->값이 감소)
#  ii-2)평균,중앙값 대체. 실제보다 작아질 수 있음
#  ii-3)예측값으로 대체
#  ii-4)시계열 특성 데이터, 결측치 대체!
# 
# 중복된 데이터
# DataFrame.duplicated():중복된 데이터 여부로 불리는 값 반환
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop_duplicates.html
# 
# DataFrame.drop_duplicates(subset=None, keep='first', inplace=False, ignore_index=False)[source]
# 
# 이상치(Outlier)
# 값의 범위에서 벗어나 극단적으로 크거나 작은 값.
# [이상치 찾는 법]
# i)score:평균과 표준편차 이용.
# 평균을 빼주고 표준편차로 나눠 z score{ (X−μ)/σ}를 계산합니다.
# zscore를 넘는 데이터는 이상치.
# 이상치 기준 작음-->판단 데이터 증가
# 이상치 기준 증가-->판단 데이터 감소
# 
# [이상치 판단법]
# 
# 1. 이상치 삭제-->따로 분석
# 2. 이상치 대체(최댓값,최솟값 설정)
# 3. 예측 모델을 만들어서 예측값 활용
# 4. binning-->수치형 데이터를 범주형으로 바꾼다.
# 
# http://colingorrie.github.io/outlier-detection.html
# 
# [z-score method]
#    <인풋>
# -데이터의 인덱스 리턴 함수:outlier
# -데이터프레임:df
# -컬럼:col
# -기준:z
# 
# abs(df[col] - np.mean(df[col])) : |데이터- 평균| 
# 
# abs(df[col] - np.mean(df[col]))/np.std(df[col]) : 작업/ 표준편차 
# 
# df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index: 값>z 추출
# 
# [IQR method(사분위범위수)]
# 
# IQR=Q3 - Q1
# 즉, IQR은 제3사분위수~ 제1사분위 값을 뺀 값으로 중간50%범위
# 이상치  기준!
#  I) Q1 - 1.5 * IRQ보다 왼쪽
#  II) Q3 + 1.5 * IRQ보다 오른쪽
#  
#  https://d3s0tskafalll9.cloudfront.net/media/images/F-19-1.max-800x600.jpg
#  
# 정규화(Normalization)
# https://realblack0.github.io/2020/03/29/normalization-standardization-regularization.html
# https://www.youtube.com/watch?v=FDCfw-YqWTE
# 
# * train 데이터와 test 데이터가 나눠져 있는 경우 train 데이터를 정규화시켰던 기준 그대로 test 데이터도 정규화 시켜줘야 합니다. *
# 
# :컬럼 간에 범위가 크게 다를 경우 데이터 정규화.
# [정규화 하는 방법]
# 1.표준화(Standardization)
#   * 데이터 평균은 0, 분산은 1
#         
#         (X−μ) / σ
# 2.Min-Max Scaling
#    * 데이터의 최솟값은 0, 최댓값은 1로 변환
#    
#    (X−Xmin) / (Xmax -Xmin)
# 3,
# scikit-learn의 
# StandardScaler, MinMaxScaler를 사용하는 방법도 있습니다.
#    
# 원-핫 인코딩(One-Hot Encoding)
# :머신 러닝이나 딥러닝 프레임워크에서 범주형 지원하지 않는 경우 이용
# :이진특성-1 / 나머지 -0
# 
# 구간화(Binning)
# :구간별로 나누기
# 
# [방법]
# 1. Data binning
# 2. bucketing
#  +cut) 구간 정하기
#  +value_counts():구간별로 값이 몇 개가 속해있는지 확인
#  +bins:정수를 입력하면 데이터의 최솟값에서 최댓값을 균등하게 bins갯수만큼 나눠준다
#  +qcut: 데이터 분포를 비슷한 크기의 그룹으로 나눠줍니다.
#  

# In[1]:


get_ipython().system(' mkdir -p ~/aiffel/data_preprocess/')
get_ipython().system(' ln -s ~/data/ ~/aiffel/data_preprocess/')


# In[2]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
print("👽 Hello.")


# In[3]:


import os

csv_file_path = os.getenv('HOME')+'/aiffel/data_preprocess/data/trade.csv'
trade = pd.read_csv(csv_file_path) 
trade.head()


# In[4]:


print('전체 데이터 건수:', len(trade))


# In[10]:


print('컬럼별 결측치 개수')
len(trade) - trade.count()


# In[12]:


trade.isnull()


# In[13]:


trade.isnull()


# In[14]:


trade[trade.isnull().any(axis=1)]


# In[15]:


trade.dropna(how='all', subset=['수출건수', '수출금액', '수입건수', '수입금액', '무역수지'], inplace=True)
print("👽 It's okay, no biggie.")


# In[16]:


trade[trade.isnull().any(axis=1)]


# In[17]:


trade.loc[[188, 191, 194]]


# In[18]:


trade.loc[191, '수출금액'] = (trade.loc[188, '수출금액'] + trade.loc[194, '수출금액'] )/2
trade.loc[[191]]


# In[26]:


trade.loc[191, '무역수지'] = trade.loc[191, '수출금액'] - trade.loc[191, '수입금액'] 
trade.loc[[191]]


# In[25]:


trade.duplicated()


# In[27]:


trade[trade.duplicated()]


# In[28]:


trade[(trade['기간']=='2020년 03월')&(trade['국가명']=='중국')]


# In[29]:


trade.drop_duplicates(inplace=True)
print("👽 It's okay, no biggie.")


# In[30]:


df = pd.DataFrame({'id':['001', '002', '003', '004', '002'], 
                   'name':['Park Yun', 'Kim Sung', 'Park Jin', 'Lee Han', 'Kim Min']})
df


# In[31]:


df.drop_duplicates(subset=['id'], keep='last')


# In[32]:


def outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col])>z].index
print("👽 It's okay, no biggie.")


# In[33]:


trade.loc[outlier(trade, '무역수지', 1.5)]


# In[35]:


trade.loc[outlier(trade, '무역수지', 1.5)]


# In[34]:


trade.loc[outlier(trade, '무역수지', 2)]


# In[36]:


trade.loc[outlier(trade, '무역수지', 3)]


# In[37]:


def not_outlier(df, col, z):
    return df[abs(df[col] - np.mean(df[col]))/np.std(df[col]) <= z].index
print("👽 It's okay, no biggie.")


# In[38]:


trade.loc[not_outlier(trade, '무역수지', 1.5)]


# In[39]:


np.random.seed(2020)
data = np.random.randn(100)  # 평균 0, 표준편차 1의 분포에서 100개의 숫자를 샘플링한 데이터 생성
data = np.concatenate((data, np.array([8, 10, -3, -5])))      # [8, 10, -3, -5])를 데이터 뒤에 추가함
data


# In[40]:


fig, ax = plt.subplots()
ax.boxplot(data)
plt.show()


# In[41]:


Q3, Q1 = np.percentile(data, [75 ,25])
IQR = Q3 - Q1
IQR


# In[42]:


dataC


# In[47]:


def outlier2(df, col):
    q1 = df[col].quantile(0.32)
    q3 = df[col].quantile(0.56)
    iqr = q3 - q1
    return df[(df[col] < q1-1.5*iqr)|(df[col] > q3+1.5*iqr)]

outlier2(trade, '무역수지')


# In[50]:


# 정규분포를 따라 랜덤하게 데이터 x를 생성합니다. 
np.random.seed(2020)
x = pd.DataFrame({'A': np.random.randn(100)*4+4,
                 'B': np.random.randn(100)-1})
x


# In[51]:


# 데이터 x를 Standardization 기법으로 정규화합니다. 
x_standardization = (x - x.mean())/x.std()
x_standardization


# In[52]:


# 데이터 x를 min-max scaling 기법으로 정규화합니다. 
x_min_max = (x-x.min())/(x.max()-x.min())
x_min_max


# In[53]:


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


# In[54]:


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


# In[55]:


# trade 데이터를 Standardization 기법으로 정규화합니다. 
cols = ['수출건수', '수출금액', '수입건수', '수입금액', '무역수지']
trade_Standardization= (trade[cols]-trade[cols].mean())/trade[cols].std()
trade_Standardization.head()


# In[56]:


trade_Standardization.describe()


# In[57]:


# trade 데이터를 min-max scaling 기법으로 정규화합니다. 
trade[cols] = (trade[cols]-trade[cols].min())/(trade[cols].max()-trade[cols].min())
trade.head()


# In[58]:


trade.describe()


# In[59]:


train = pd.DataFrame([[10, -10], [30, 10], [50, 0]])
test = pd.DataFrame([[0, 1], [10, 10]])
print("👽 It's okay, no biggie.")


# In[60]:


train_min = train.min()
train_max = train.max()

train_min_max = (train - train_min)/(train_max - train_min)
test_min_max =  (test - train_min)/(train_max - train_min)    # test를 min-max scaling할 때도 train 정규화 기준으로 수행
print("💫 It's okay, no biggie...")


# In[61]:


train_min_max


# In[62]:


test_min_max


# In[63]:


from sklearn.preprocessing import MinMaxScaler
train = [[10, -10], [30, 10], [50, 0]]
test = [[0, 1]]
scaler = MinMaxScaler()
print("👽 It's okay, no biggie.")


# In[64]:


scaler.fit_transform(train)


# In[65]:


scaler.transform(test)


# In[66]:


#trade 데이터의 국가명 컬럼 원본
print(trade['국가명'].head())  

# get_dummies를 통해 국가명 원-핫 인코딩
country = pd.get_dummies(trade['국가명'])
country.head()


# In[67]:


trade = pd.concat([trade, country], axis=1)
trade.head()


# In[71]:


salary = pd.Series([4300, 8370, 1750, 3830, 1840, 4220, 3020, 2290, 4740, 4600, 
                    2860, 3400, 4800, 4470, 2440, 4530, 4850, 4850, 4760, 4500, 
                    4640, 3000, 1880, 4880, 2240, 4750, 2750, 2810, 3100, 4290, 
                    1540, 2870, 1780, 4670, 4150, 2010, 3580, 1610, 2930, 4300, 
                    2740, 1680, 3490, 4350, 1680, 6420, 8740, 8980, 9080, 3990, 
                    4960, 3700, 9600, 9330, 5600, 4100, 1770, 8280, 3120, 1950, 
                    4210, 2020, 3820, 3170, 6330, 2570, 6940, 8610, 5060, 6370,
                    9080, 3760, 8060, 2500, 4660, 1770, 9220, 3380, 2490, 3450, 
                    1960, 7210, 5810, 9450, 8910, 3470, 7350, 8410, 7520, 9610, 
                    5150, 2630, 5610, 2750, 7050, 3350, 9450, 7140, 4170, 3090])
print("👽 Almost there..")


# In[72]:


salary.hist()


# In[73]:


bins = [0, 2000, 4000, 6000, 8000, 10000]
print("👽 Almost there..")


# In[74]:


ctg = pd.cut(salary, bins=bins)
ctg


# In[75]:


print('salary[0]:', salary[0])
print('salary[0]가 속한 카테고리:', ctg[0])


# In[76]:


ctg.value_counts().sort_index()


# In[77]:


ctg = pd.cut(salary, bins=6)
ctg


# In[78]:


ctg.value_counts().sort_index()


# In[79]:


ctg = pd.qcut(salary, q=5)
ctg


# In[80]:


print(ctg.value_counts().sort_index())
print(".\n.\n🛸 Well done!")


# In[ ]:




