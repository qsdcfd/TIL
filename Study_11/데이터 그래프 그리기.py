#!/usr/bin/env python
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

# 그래프 데이터 
subject = ['English', 'Math', 'Korean', 'Science', 'Computer']
points = [40, 90, 50, 60, 100]

# 축 그리기
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

# 그래프 그리기
ax1.bar(subject, points)

# 라벨, 타이틀 달기
plt.xlabel('Subject')
plt.ylabel('Points')
plt.title("Yuna's Test Result")

# 보여주기
plt.savefig('./barplot.png')  # 그래프를 이미지로 출력
plt.show()                    # 그래프를 화면으로 출력


# https://studymake.tistory.com/601

# In[ ]:


from datetime import datetime
import pandas as pd
import os

# 그래프 데이터 
csv_path = os.getenv("HOME") + "/aiffel/data_visualization/data/AMZN.csv"
data = pd.read_csv(csv_path ,index_col=0, parse_dates=True)
price = data['Close']

# 축 그리기 및 좌표축 설정
fig = plt.figure()
ax = fig.add_subplot(1,1,1)
price.plot(ax=ax, style='black')
plt.ylim([1600,2200])
plt.xlim(['2019-05-01','2020-03-01'])

# 주석달기
important_data = [(datetime(2019, 6, 3), "Low Price"),(datetime(2020, 2, 19), "Peak Price")]
for d, label in important_data:
    ax.annotate(label, xy=(d, price.asof(d)+10), # 주석을 달 좌표(x,y)
                xytext=(d,price.asof(d)+100), # 주석 텍스트가 위차할 좌표(x,y)
                arrowprops=dict(facecolor='red')) # 화살표 추가 및 색 설정

# 그리드, 타이틀 달기
plt.grid()
ax.set_title('StockPrice')

# 보여주기
plt.show()


# <Pandas로 그래프 그리기>
# 
# 
# # pandas.plot메서드 인자
# 
# label: 그래프의 범례이름.
# ax: 그래프를 그릴 matplotlib의 서브플롯 객체.
# style: matplotlib에 전달할 'ko--'같은 스타일의 문자열
# alpha: 투명도 (0 ~1)
# kind: 그래프의 종류: line, bar, barh, kde
# logy: Y축에 대한 로그스케일
# use_index: 객체의 색인을 눈금 이름으로 사용할지의 여부
# rot: 눈금 이름을 로테이션(0 ~ 360)
# xticks, yticks: x축, y축으로 사용할 값
# xlim, ylim: x축, y축 한계
# grid: 축의 그리드 표시할 지 여부
# # pandas의 data가 DataFrame일때 plot 메서드 인자
# 
# subplots: 각 DataFrame의 칼럼을 독립된 서브플롯에 그린다.
# sharex: subplots=True면 같은 X축을 공유하고 눈금과 한계를 연결한다.
# sharey: subplots=True면 같은 Y축을 공유한다.
# figsize: 그래프의 크기, 튜플로 지정
# title: 그래프의 제목을 문자열로 지정
# sort_columns: 칼럼을 알파벳 순서로 그린다.

# 그래프를 그리는 과정을 다시 정리해 봅시다.
# 
# 1)
# fig = plt.figure(): figure 객체를 선언해 '도화지를 펼쳐' 줍니다.
# 2)
# ax1 = fig.add_subplot(1,1,1) : 축을 그립니다.
# 3)
# ax1.bar(x, y) 축안에 어떤 그래프를 그릴지 메소드를 선택한 다음, 인자로 데이터를 넣어줍니다.
# 4)
# 그래프 타이틀 축의 레이블 등을 plt의 여러 메소드 grid, xlabel, ylabel 을 이용해서 추가해주고
# 5)
# plt.savefig 메소드를 이용해 저장해 줍니다.
# 어떤가요? 현실세계에서 그래프를 그리는 순서와 유사하지 않나요? 꽤 직관적입니다.
# 
# 파이썬 기반의 시각화 라이브러리인 Pandas, Matplotlib, Seaborn 모두 이런 식으로 그래프를 그립니다.
# 
# 아래 그림은 각 그래프 요소별 명칭입니다. 눈에 익혀 두세요.
# 
# https://d3s0tskafalll9.cloudfront.net/media/images/F-15-2.max-800x600.png
# 
# <다양한 데이터 그리기>
# LMS 8번 참고
