#!/usr/bin/env python
# coding: utf-8

# 목차
# 1.파이썬으로 그래프를 그린다는건?
# 2.간단한 그래프 그리기
# 3.그래프 4대 천왕: 막대그래프, 선그래프, 산점도, 히스토그램
# 4.시계열 데이터 시각화하기
# 5.Heatmap
# 

# In[1]:


get_ipython().system(' pip list | grep matplotlib')
get_ipython().system(' pip list | grep seaborn')


# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
fig = plt.figure() #도화지(그래프) 객체 생성
ax1 = fig.add_subplot(1,1,1) #figure()객체에 add_subplot 메소드를 이용해 축을 그려준다.

# 그래프 그리기
ax1.bar(subject, points)

# 라벨, 타이틀 달기
plt.xlabel('Subject')
plt.ylabel('Points')
plt.title("Yuna's Test Result")

# 보여주기
plt.savefig('./barplot.png')  # 그래프를 이미지로 출력
plt.show()                    # 그래프를 화면으로 출력


# In[ ]:


get_ipython().run_line_magic('matplotlib', 'inline은 매직 메소드 in IPython')
-->그래프와 그림같은 애니매이션 
결과물(rich output)일 때 사용
https://studymake.tistory.com/601


# In[5]:


fig = plt.figure()
ax1 = fig.add_subplot(2,2,1) # 2,2는 2행 2열로 총 4개
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,4)


# In[9]:


# 아마존 주가 데이터 이용 https://finance.yahoo.com/quote/AMZN/history?p=AMZN

from datetime import datetime
import pandas as pd
import os

# 그래프 데이터 
csv_path = os.getenv("HOME") + "/aiffel/data_visualization/data/AMZN.csv"
data = pd.read_csv(csv_path ,index_col=0, parse_dates=True)
price = data['Close'] #Pandas 의 Series

# 축 그리기 및 좌표축 설정
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
price.plot(ax=ax, style='black')#Pandas의 plot 사용,matplotlib의 subplot 공간 ax사용

plt.ylim([1600,2200])#y좌표축의 적당 범위 설정
plt.xlim(['2019-05-01','2020-03-01'])#x좌표축의 적당 범위 설정

# 주석달기
important_data = [(datetime(2019, 6, 3), "Low Price"),(datetime(2020, 2, 19), "Peak Price")]
for d, label in important_data:
    ax.annotate(label, xy=(d, price.asof(d)+10), # 주석을 달 좌표(x,y)
                xytext=(d,price.asof(d)+100), # 주석 텍스트가 위차할 좌표(x,y)
                arrowprops=dict(facecolor='red')) # 화살표 추가 및 색 설정

# 그리드, 타이틀 달기
plt.grid()#격자 눈금 추가
ax.set_title('StockPrice')

# 보여주기
plt.show()


# <Pandas Series데이터 활용>
# 1.선 그래프 그리기에 최적구조https://nittaku.tistory.com/110
# 
# 2. pit.plot()로 그래프 그리기
# figure()객체 생성 + add_subplot() 서브 플릇 생성
# -->plot 그림
# ---> 생략하는 법
# plt.plot()명령어-->matplotlib은 가장 최근figure객체와
# 서브플룻 그림
# plt.subplot() # 서브 플룻 추가
# 
# 3.linestyle, marker옵션
# plot()인자로 들어가게 되는데 다양하게 표현 가능
# 
# 4.Pandas로 그래프 그리기
# 
# pandas.plot메서드 인자
# 
# label: 그래프의 범례이름.
# 
# ax: 그래프를 그릴 matplotlib의 서브플롯 객체.
# 
# style: matplotlib에 전달할 'ko--'같은 스타일의 문자열
# 
# 
# alpha: 투명도 (0 ~1)
# 
# kind: 그래프의 종류: line, bar, barh, kde
# 
# logy: Y축에 대한 로그스케일
# 
# use_index: 객체의 색인을 눈금 이름으로 사용할지의 여부
# 
# rot: 눈금 이름을 로테이션(0 ~ 360)
# 
# xticks, yticks: x축, y축으로 사용할 값
# 
# xlim, ylim: x축, y축 한계
# 
# grid: 축의 그리드 표시할 지 여부
# 
# 5.pandas의 data가 DataFrame일 때 plot 메서드 인자
# 
# subplots: 각 DataFrame의 칼럼을 독립된 서브플롯에 그린다.
# 
# sharex: subplots=True면 같은 X축을 공유하고 눈금과 한계를 연결한다.
# 
# sharey: subplots=True면 같은 Y축을 공유한다.
# 
# figsize: 그래프의 크기, 튜플로 지정
# 
# title: 그래프의 제목을 문자열로 지정
# 
# sort_columns: 칼럼을 알파벳 순서로 그린다.
# 
# 6. 정리!
# i)
# fig = plt.figure(): figure 객체를 선언해 '도화지를 펼쳐' 줍니다.
# 
# ii)
# ax1 = fig.add_subplot(1,1,1) : 축을 그립니다.
# 
# iii)
# ax1.bar(x, y) 축안에 어떤 그래프를 그릴지 메소드를 선택한 다음, 인자로 데이터를 넣어줍니다.
# 
# iv)
# 그래프 타이틀 축의 레이블 등을 plt의 여러 메소드 grid, xlabel, ylabel 을 이용해서 추가해주고
# 
# v)
# plt.savefig 메소드를 이용해 저장해 줍니다.

# In[10]:


import numpy as np
x = np.linspace(0, 10, 100) #0에서 10까지 균등한 간격으로  100개의 숫자를 만들라는 뜻입니다.
plt.plot(x, np.sin(x),'o')
plt.plot(x, np.cos(x),'--', color='black') 
plt.show()


# In[11]:


x = np.linspace(0, 10, 100) 

plt.subplot(2,1,1)
plt.plot(x, np.sin(x),'orange','o')

plt.subplot(2,1,2)
plt.plot(x, np.cos(x), 'orange') 
plt.show()


# In[12]:


x = np.linspace(0, 10, 100) 

plt.plot(x, x + 0, linestyle='solid') 
plt.plot(x, x + 1, linestyle='dashed') 
plt.plot(x, x + 2, linestyle='dashdot') 
plt.plot(x, x + 3, linestyle='dotted')
plt.plot(x, x + 0, '-g') # solid green 
plt.plot(x, x + 1, '--c') # dashed cyan 
plt.plot(x, x + 2, '-.k') # dashdot black 
plt.plot(x, x + 3, ':r'); # dotted red
plt.plot(x, x + 4, linestyle='-') # solid 
plt.plot(x, x + 5, linestyle='--') # dashed 
plt.plot(x, x + 6, linestyle='-.') # dashdot 
plt.plot(x, x + 7, linestyle=':'); # dotted


# In[13]:


fig, axes = plt.subplots(2, 1)
data = pd.Series(np.random.rand(5), index=list('abcde'))
data.plot(kind='bar', ax=axes[0], color='blue', alpha=1)
data.plot(kind='barh', ax=axes[1], color='red', alpha=0.3)


# In[14]:


df = pd.DataFrame(np.random.rand(6,4), columns=pd.Index(['A','B','C','D']))
df.plot(kind='line')


# 1.데이터 불러오기
# https://github.com/mwaskom/seaborn-data
# 
# load_dataset()메소드 이용
# default directory: ~/seaborn-data/ (~(물결표시)는 home directory를 의미합니다.)
# 
# https://leedakyeong.tistory.com/entry/%EC%88%98%EC%B9%98%ED%98%95-%EC%9E%90%EB%A3%8Cnumerical-data%EC%99%80-%EB%B2%94%EC%A3%BC%ED%98%95-%EC%9E%90%EB%A3%8Ccategorical-data
# 
# * 범주(catrgory)형 데이터
# :주로 막대 그래프(가로,세로 그룹화),수치요약
# :sex, smoker, day, time
# * 수치형 데이터
# : 산점도(scatter plot) 혹은 선그래프 이용
# : tips,total_bill, size
#  +) Numpy데이터 형태
# https://rfriend.tistory.com/285

# In[15]:


#https://github.com/mwaskom/seaborn-data/blob/master/tips.csv

import pandas as pd
import seaborn as sns
tips = sns.load_dataset("tips")


# In[18]:


df = pd.DataFrame(tips)
df.head()


# In[21]:


df = pd.DataFrame(tips)
df.shape


# In[22]:


df.describe()


# In[23]:


df.describe()


# In[24]:


print(df['sex'].value_counts())
print("===========================")


print(df['time'].value_counts())
print("===========================")


print(df['smoker'].value_counts())
print("===========================")


print(df['day'].value_counts())
print("===========================")


print(df['size'].value_counts())
print("===========================")


# In[30]:


# Pandas와 Matplotlib를 활용한 방법 
#df의 첫 5행을 확인해봅시다. 
df.head()


# In[28]:


grouped = df['tip'].groupby(df['sex'])#각 성별 그룹에 대한 정보


# In[29]:


grouped.mean() # 성별에 따른 팁의 평균


# In[31]:


grouped.size() # 성별에 따른 데이터 량(팁 횟수)


# In[33]:


import numpy as np
sex = dict(grouped.mean()) #평균 데이터를 딕셔너리 형태로 바꿔줍니다.
sex


# In[36]:


x = list(sex.keys())  


# In[35]:


y = list(sex.values())
y


# In[37]:


import matplotlib.pyplot as plt

plt.bar(x = x, height = y)
plt.ylabel('tip[$]')
plt.title('Tip by Sex')


# Seaborn을 이용하면 더 쉽게 나타낼 수 있습니다.
# 
# sns.barplot의 인자로 df를 넣고 원하는 
# 컬럼을 지정해 주면
# 
# 아래와 같이 성별에 대한 tip 평균을 볼 수 있습니다.
# 
# Matplot과 함께 사용하여 figsize, title을 정하는 등 그래프에 다양한 옵션을 넣을 수도 있어요.
# 
# Subplot을 활용할 수도 있고, 
# 범주형 그래프를 나타내기에 좋은 violineplot을 사용할 수도 있습니다.
# 
# palette 옵션을 주어 더 예쁜 색상을 사용할 수도 있어요.

# In[38]:


# Seaborn과 Matplotlib을 활용한 간단한 방법
sns.barplot(data=df, x='sex', y='tip')


# In[39]:


plt.figure(figsize=(10,6)) # 도화지 사이즈를 정합니다.
sns.barplot(data=df, x='sex', y='tip')
plt.ylim(0, 4) # y값의 범위를 정합니다.
plt.title('Tip by sex') # 그래프 제목을 정합니다.


# In[40]:


plt.figure(figsize=(10,6))
sns.barplot(data=df, x='day', y='tip')
plt.ylim(0, 4)
plt.title('Tip by day')


# In[41]:


fig = plt.figure(figsize=(10,7))

ax1 = fig.add_subplot(2,2,1)
sns.barplot(data=df, x='day', y='tip',palette="ch:.25")

ax2 = fig.add_subplot(2,2,2)
sns.barplot(data=df, x='sex', y='tip')

ax3 = fig.add_subplot(2,2,4)
sns.violinplot(data=df, x='sex', y='tip')

ax4 = fig.add_subplot(2,2,3)
sns.violinplot(data=df, x='day', y='tip',palette="ch:.25")


# In[42]:


sns.catplot(x="day", y="tip", jitter=False, data=tips)


# In[43]:


#산점도 그래프
sns.scatterplot(data=df , x='total_bill', y='tip', palette="ch:r=-.2,d=.3_r")


# In[44]:


sns.scatterplot(data=df , x='total_bill', y='tip', hue='day')


# In[45]:


# 선 그래프
#np.random.randn 함수는 표준 정규분포에서 난수를 생성하는 함수입니다. 
#cumsum()은 누적합을 구하는 함수입니다.
plt.plot(np.random.randn(50).cumsum())


# In[46]:


x = np.linspace(0, 10, 100) 
plt.plot(x, np.sin(x), 'o')
plt.plot(x, np.cos(x)) 
plt.show()


# In[47]:


#Seaborn활용
sns.lineplot(x, np.sin(x))
sns.lineplot(x, np.cos(x))


# <히스토그램>
# :도수분포표로 그래프 나타냄.
# -가로축
#   +)계급: 변수의 구간, bin(or bucket)
# -세로축
#   +)도수: 빈도수, frequency
# -전체 총량:n

# In[48]:


#x1평균:100,표준편차:15
#x2평균:130,표준편차:15
#도수를 50 구간, 빈도로 표기

#그래프 데이터 
mu1, mu2, sigma = 100, 130, 15
x1 = mu1 + sigma*np.random.randn(10000)
x2 = mu2 + sigma*np.random.randn(10000)

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
patches = ax1.hist(x1, bins=50, density=False) #bins는 x값을 총 50개 구간으로 나눈다는 뜻입니다.
patches = ax1.hist(x2, bins=50, density=False, alpha=0.5)
ax1.xaxis.set_ticks_position('bottom') # x축의 눈금을 아래 표시 
ax1.yaxis.set_ticks_position('left') #y축의 눈금을 왼쪽에 표시

# 라벨, 타이틀 달기
plt.xlabel('Bins')
plt.ylabel('Number of Values in Bin')
ax1.set_title('Two Frequency Distributions')

# 보여주기
plt.show()


# In[49]:


sns.distplot(df['total_bill'], label = "total_bill")
sns.distplot(df['tip'], label = "tip").legend()# legend()를 이용하여 label을 표시해 줍니다.


# 예제 데이터의 히스토그램
# 조금 복습이 되셨나요? 다시 예제의 tips 데이터로 돌아가서 tips 데이터의 total_bill과 tips에 대해 히스토그램을 만들어 보겠습니다.
# 
# 

# In[51]:


df['tip_pct'] = df['tip'] / df['total_bill']
df['tip_pct'].hist(bins=50)


# In[52]:


#'kde=확률 밀도 그래프(연속된 확률 분포)'

df['tip_pct'].plot(kind='kde')


# 일반적으로는 kernels메서드를 섞어서 이 분포를 근사하는 식으로 그립니다.
# 이것은 좀 더 단순하고 우리에게 친숙한 정규분포(가우시안)로 나타낼 수 있습니다.
# 위 밀도 그래프는 KDE(Kernel Density Estimate) 커널 밀도 추정 그래프입니다.
# https://darkpgmr.tistory.com/147#:~:text=Kernel%20Density%20Estimation%20(%EC%BB%A4%EB%84%90%20%EB%B0%80%EB%8F%84%20%EC%B6%94%EC%A0%95)%20%EB%B0%A9%EB%B2%95%EC%9D%80%20non%2D,%EC%9D%84%20%EA%B0%9C%EC%84%A0%ED%95%9C%20%EB%B0%A9%EB%B2%95%EC%9D%B4%EB%8B%A4.

# <시계열 데이터 시각화 하기>
# 1.데이터 가져오기
# 2.그래프 그리기
# +)히스토그램

# In[53]:


csv_path = os.getenv("HOME") + "/aiffel/data_visualization/data/flights.csv"
data = pd.read_csv(csv_path)
flights = pd.DataFrame(data)
flights


# In[54]:


sns.barplot(data=flights, x='year', y='passengers')


# In[55]:


sns.pointplot(data=flights, x='year', y='passengers')


# In[56]:


sns.lineplot(data=flights, x='year', y='passengers')


# In[57]:


sns.lineplot(data=flights, x='year', y='passengers', hue='month', palette='ch:.50')
plt.legend(bbox_to_anchor=(1.03, 1), loc=2) #legend 그래프 밖에 추가하기


# In[58]:


sns.distplot(flights['passengers'])


# [Heatmap]
# :방대한 양의 데이터와 현상을 수치에 따른 색으로 나타냄
# 데이터 차원에 대한 제한은 없으나 모두2차원 시각화
# 
# ❗잠깐만! pivot
# 
# Heatmap을 그리기 위해 데이터를 pivot해야 하는 경우가 있습니다.
# 
# pivot이란 어떤 축, 점을 기준으로 바꾸다란 뜻입니다. 데이터 표를 재배치 할때도 pivot이라는 단어를 사용합니다. (엑셀, Database에도 등장하는 용어 입니다.)

# In[59]:


pivot = flights.pivot(index='year', columns='month', values='passengers')
pivot


# In[60]:


sns.heatmap(pivot)


# In[69]:


sns.heatmap(pivot,linewidths=.2 ,annot=True,fmt="d")


# In[62]:


sns.heatmap(pivot, cmap="YlGnBu")


# In[ ]:




