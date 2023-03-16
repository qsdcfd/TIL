회귀(Regression)
*정의: 주어진 데이터(X, input data[feature vector])와 찾고 싶은 값(y, target value[real value]) 사이의 관계를 찾아서 모델링하는 것이다.

*특징

- input data(독립변수)로 target value(종속변수)를 예측하는 것을 목표로 하고, 이를 위해서 관계식을 작성하고 이를 통해 모델링을 하는 것이 분석의 목표이다.



- 머신러닝 모델이 관계식을 찾게 되면, 해당 관계식에 test data를 inference한 결과가 예측
값(결과값)이다.



- 지도학습이기에, target value를 찾는 방향으로 학습이 진행된다.



수식과 코드로 보는 회귀분석
%config InlineBackend.figure_formats = {'png', 'retina'}
import pandas as pd 
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

#샘플 데이터 생성
datas = np.array([[1,3], [2,5], [3,7]])
df = pd.DataFrame(datas, columns=list('xy'))
df

#산점도 그리기
plt.scatter(df['x'], df['y'])
plt.xticks(range(0,8))
plt.yticks(range(0,8))
plt.show()





이제 점들의 흐름을 알아보기 위해서 추세선을 그릴 것입니다. 

추세선을 그리는 이유는 현재 데이터의 흐름을 파악하기 위해서입니다.

#추세선을 구하는 방법: 방정식

data = [1,2,3]
result = [num**2 for num in data if num %2]
result#[1,9]

##추세선 함수:y = 1+2x
def pred_func(x):
	return 1 + 2 * x

##예측값 구하기
pred_y = [pred_func(data) for data in range(0,5)]
pred_y #[1,3,5,7,9]

##추세선 그리기
plt.scatter(df['x'], df['y'])
plt.plot(range(0,5), pred_y, 'r-')
plt.xticks(range(0,10))
plt.yticks(range(0,10))
plt.show()



점들이 한 직선 위에 있으니 이쁜 추세선이 만들어졌지만 실제로 데이터들은 한 직선 위에 있는 경우가 많이 없어서 이러한 그래프들이 주로 그려집니다.




그렇다면, 데이터에 따라서 추세선들이 여러 가지가 생길 수도 있을텐데.. 매번 함수랑 점의 좌표를 그려가면서 구하기에는 resource를 낭비하는 것과 같습니다. 



그래서, 나오게 된 방법이 최소제곱법(Least Square Method)입니다.



최소제곱법

- 최적의 추세선을 구하기 위한 방법

- 오차 = 실제값 - 예측값

- 오차가 가장 작은 것이 가장 좋은 추세선이다.


데이터의 오차를 구하는 수식


- 수식 설명



1. 오차 = 실제값 - 예측값

2. 1번 부분의 좌변/우변을 제곱

3. 실제값과 예측값 그리고 오차의 합(이미지의 첫 부분 완성)

4. 예측값의 함수(이미지의 두 번째 줄)

5. 최적의 추세선 수식(이미지의 세번째 줄)



- 제곱을 하는 이유



1. 오차는 음수도 있고 양수도 있는데 제곱을 하지 않고 더할 시 0에 가까운 수가 나오게 되는 오류를 범하게 됩니다.

2. 절댓값으로하면 수치도 작고 더 편한데 제곱을 하는 이뉴는 최소 오차를 구할 때 미분을 활용하기 때문에 편한 미분을 하기 위해서 제곱을 한 것입니다.



#오차의 제곱합이 가장 작아지는 a와b를 구하는 방법1: 특정 범위에서 a와 b를 증가시켜가면서 최적의 a와 b를 찾는다.
def error_func(df, a =0, b=1):
	e = 0
    for idx, data in df.iterrows():
    	e += (data.y-a-b*data.x) **2
    return e
    
  batch_size = 0.5#batch_size, epoch
  
  a_datas = np.arange(0,3,batch_size)
  b_datas = np.arange(0,3,batch_size)
  
  error_datas = []
  
  for a_data in a_datas:
  	for b_data in b_datas:
    	error_datas.appen({
        	"a_data": a_data,
            "b_data": b_data,
            "error": error_func(df, a_data, b_data),
        })
        
   error_df = pd.DataFrame(error_datas)
   error_df
   
   #에러의 최소값
   error_df[error_df.error ==np.min(error_df.error)]


오차의 제곱합이 가장 작아지는 a와 b를 구하는 방법2: 경사하강법



경사하강법은 a와 b의 미분값으로 기울기를 구합니다.
기울기가 음수이면 값이 증가(오른쪽이동)
기울기가 양수이면 값이 감소(왼쪽으로 이동)
추세선의 수식을 예측값=bx로 가정: 경사하강법의 이해를 돕기 위해 a제거
a를 제거하는 이유는 y의 절편(a)은 기울기에 영향을 주지 않기에 제거하는 것입니다.

b값의 따른 오차가 됩니다.


b_datas = np.arange(0,5,0.5)

#에러 함수
def error_func(df, b=1):
	e=0
    for idx, data in df.iterrows():
    	e+= (data.y-b *data.x) **2
    return e
   
error_datas = []

#0~4.5까지 에러 출력
for b_data in b_datas:
	
    e = error_func(df, b_data)
    
    error_datas.append({
    	"b_data":b_data,
        "error":e,
    })
    
#b값이 2.5일때 가장 오차제곱합이 가장 작다
#그러므로 최적의 추세선은 y=2.5x

error_df = pd.DataFrame(error_datas)
error_df

#최적값
error_df[error_df.error == np.min(error_df.error)]

#b값에 대한 error값의 그래프
#그래프에서 기울기가 가장 작아지는 값이 최적의 b값이 된다.
plt.scatter(error_df.b_data, error_df.error)
plt.show()


##기울기를 구하는 함수
def slope_func(df,b):
	slope=0
    for idx, data in df.iterrows():
    	slope += -2 * (data.y - b*data.x) * data.x
    return round(slope,2)


OLS(Ordinary Least Square)
- 실제로 코드와 함께 자세히는 뒤에서 설명할 것입니다.

- 최소 제곱법으로 구해진 추세선은 평균을 지나게 됩니다.

- 추세선이 평균으로의 회귀이기에 회귀 분석입니다.

회귀분석의 총 정리
- 단순 선형회귀 분석은 하나의 x데이터로 y데이터를 예측하기 위해 최적의 추세선 수식을 구함

- x데이터로 y데이터를 예측: y=a + bx +e(오차)

- 가장 작은 오차(e)를 갖도록하는 a와b를 구하는 것이 목적

- 최소제곱법: 가장 오차가 작은 추세선을 구하는 방법

- 경사하강법: 효율적으로 b값을 구하는 방법



이제부터 다양한 상황의 회귀 모델에 대해서 설명할 것입니다.

Model1: Linear Regression
정의: y=Wx+b로 표시되는 하나의 선형식으로 x와 y사이의 관계를 찾는 모델로 회귀이기에 결과값 =예측값입니다.



식 전개: y=Wx+b (W:가중치, x:입력 값, b: bias로 미분 시 0 혹은 함수가 0을 지나지 않게 도와줌)



y = w1*x1 + w2*x2 + w3*x3 + w4*x4 +...+ wn*xn + b 



Linear classifier처럼 처음에는 랜덤 값을 가지는 가중치 wi를 통해서 예측을 수행하지만 정말 운이 좋은 경우가 아니면 실제 값과 맞지 않을 것입니다.



그러한 이유로, 이 예측 값이 실제와 가까워지려면 Gradient Descent Algorithm을 활용하여 파라미터(w,b) 업데이트 해야하는데, 이때 방향은 Loss function이 최소가 되는 지점으로 향합니다.



장점

- 통계적으로 설명 가능한 이론이 많다.

- 수식이 복잡하지 않은 선형식이므로 직접 계산을 하여 예측값이 왜 나오는지 설명 가능하다.

- 복잡한 모델보다 예측력이 뛰어나다.

MSE(Mean Squared Error)

- 회귀에서 가장 많이 사용되는 Loss function

- optimal solution을 찾을 수 있다.

- 모델의 예측값이 실제값에 점점 가까워지게 학습하여 전제척으로 Loss의 평균이 작아지는 방향으로 학습한다.

- 이상치에 민감하기에 미리 제거 혹은 보정 후에 활용해야함



코드로 보는 Linear Regression
프리미어리그의 승점 예측

#데이터 부르기
%config InlineBackend.figure_formats = {'png', 'retina'}
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

with open("./data/premierleague.pkl", "rb") as file:
    datas = pickle.load(file)

df = pd.DataFrame(datas, columns=["name", "gf", "ga", "points"])
df.tail(2)

#데이터 처리: feature, target 데이터 분리
feature_gf = df[['gf']] #승점예측과 관련된 것
feature_ga = df[['ga']] #승점예측과 관련된 것
target = df['points'] #승점

#모델링:모델학습해서 만들기
from sklearn.linear_model import LinearRegression
model_gf = LinearRegression()
model_gf.fit(feature_gf, target)

#모델 성능평가: MAE, RMSE, MAE, MAPE
#MAE
from sklearn.metrics import mean_absolute_error
pred = np.round(model_gf.predict(feature_gf))
feature_gf.values[:5,0], pred[:5,0] , pred[:5], target.values[:5]

#MAE
mean_absolute_error(target, pred) #5.5


# 모델 사용
# Leicester City	56	60	47
# 득점이 60점이였으면 승점이 몇점이였을까?
np.round(model_gf.predict([[60]]))


# 7. 실점으로 모델 만들기
# feature_ga, target
model_ga = LinearRegression()
model_ga.fit(feature_ga, target)

pred = np.round(model_ga.predict(feature_ga))
mean_absolute_error(target, pred) # 득점 MAE : 5.5 , 실점:8.05


#회귀계수 확인
model_gf.coef_, model_gf.intercept_

model_ga.coef_, model_ga.intercept_

for column in ["gf", "ga", "points"]:
    df[column] = df[column].astype("int")

with open("datas/advertising.pkl", "rb") as file:
    datas = pickle.load(file)

df = pd.DataFrame(datas, columns=["tv", "radio", "newspaper", "sales"])
df.tail(2)

model_combined = LinearRegression()

features = pd.concat([feature_gf, feature_ga], axis=1)
print(features)

pred_combined = np.round(model_combined.predict(features))
mean_absolute_error(target, pred_combined) #2.9

model_combined.fit(features, target)


회귀 모델 성능 평가 지표(MAE, MSE, RMSE, MAPE 등)
회귀모델에서는 얼마나 정확하게 예측했는지가 중요하기에 동일하게 예측하면 가장 좋고 그렇지 않을 경우 가자 가깝게 예측하는 것이 좋다.

MAE(Mean Absolute Error) = 평균 절대 오차

특징



- 실제 정답값과 예측값의 차이를 절댓값으로 변환하여 합산을 한 후 평균 구한다.

- Error에 절대값을 취하기 때문에 에러의 크기를 그대로 반영한다.

- 에러에 따른 손실이 선형적으로 올라갈 때 적합하다

- 이상치가 많을 경우 주로 사용된다.

- 값이 낮을 수록 좋다.





단점



- 실제 정답보다 낮게 예측했는지 높게 예측했는지 파악하기 어렵다.

- 스케일 의존적: 모델마다 오류 크기가 동일해도 오류율이 동일하지 않다.

from sklearn.metrics import mean_absolute_error
mean_absolute_error(y_test, y_pred)

MSE(Mean Squared Error) = 평균 제곱 오차

특징



- 실제 정답값과 예측값의 차이를 제곱한 뒤 평균을 구한다.

- 특이값이 존재하면 수치가 많이 늘어난다.

- 에러에 제곱을 하기 때문에 에러가 클수록 그에 따른 가중치가 높이 반영된다.



단점



- 제곱하기 때문에 1미만의 에러는 작아지고, 그 이상의 에러는 커진다.

- 실제 정답보다 낮게 예측했는지 높게 예측했는지 파악하기 어렵다.

- 스케일 의존적: 모델마다 오류 크기가 동일해도 오류율이 동일하지 않다.

from sklearn.metrics import mean_squared_error 
mean_squared_error(y_test, y_pred)





RMSE(Root Mean Squared Error) = 평균 제곱근 오차

특징



- MSE에 루트를 씌웠기에 에러를 제곱해서 생기는 값의 왜곡이 줄어든다.

- 값이 낮을 수록 좋다

- MAE와 함께 가장 일반적으로 많이 쓰이는 회귀모델 성능분석지표

- 에러에 따른 손실이 기하급수적으로 올라가는 상황에 쓰기 적합하다.



단점



- 실제 정답값과 예측값의 차이를 제곱한 뒤 평균을 구한다.

- 특이값이 존재하면 수치가 많이 늘어난다.

- 스케일 의존적: 에러에 제곱을 하기 때문에 에러가 클수록 그에 따른 가중치가 높이 반영된다.

from sklearn.metrics import mean_squared_error 
MSE = mean_squared_error(y_test, y_pred) 
np.sqrt(MSE)


MAPE(Mean Absolute Percentage Error) = 평균 절대 비율 오차

특징



- MAE를 비율, 퍼센트로 표현하여 스케일 의존적 에러의 문제점 개선한다.

- 값이 낮을수로 좋다.

- 비율 변수이기 때문에 MAE, MSE, RMSE에 비해 다른 모델과 에러율 비교가 쉽다.

- 지표 자체가 직관적이다.

   - EX) MAPE=3%일 경우 예매량과 예측 예매량 비율이 3%정도 차이가 난다고 해석이 가능하다.



단점



- 실제 정답보다 낮게 예측했는지, 높게 했는지 파악하기가 어렵다


- 실제 정답이 1보다 작을 경우, 무한대의 값으로 수렴한다.

- 비율로 해석이 의미있는 값에만 적용이 가능하다.

- 실제 값에 0이 포함이 된 경우 MAPE계산이 불가하다.

- 모델에 대한 편향이 존재한다.

- MAE의 단점을 그대로 갖고 있다



def MAPE(y_test, y_pred):
	return np.mean(np.abs((y_test - y_pred) / y_test)) * 100 
    
MAPE(y_test, y_pred)



MPE(Mean Percentage Error)

특징



- MAPE에서 절대값을 제외하여 계산한다.

- 모델이 underperformance(+) 인지 overperformance(-) 인지 판단한다.

- 음수이면 overperformance이다

- 양수이면 underperformance이다



def MAE(y_test, y_pred): 
	return np.mean((y_test - y_pred) / y_test) * 100)
    
MAE(y_test, y_pred)

R2 score를 가기 전에 지금까지 배운 내용을 코드로 구현해보겠습니다.



캐글 데이터를 활용했습니다.


Google Colaboratory Notebook

Run, share, and edit Python notebooks

colab.research.google.com


R2 score = R squard

특징



- 독립변수가 종속변수를 얼마나 설명을 해주는 지표로 설명력이라고 불린다.

- 결정계수가 높다면 독립변수가 종속변수를 많이 설명하는 것이므로 독립변수가 증가하면 결정계수도 높아집니다.

- 상대적인 성능을 나타내기에 비교가 쉽다.

- 실제 값의 분산 대비 예측값의 분산 비율을 의미한다.

- 1에 가까울수록 좋다



단점



- 의미없는 독립변수의 개수가 증가하면 일방적으로 결정계수가 증가하기도 한다.

- 위의 문제로 회귀 모델의 유용성 판단을 할 시 문제가 생긴다.


선형 직선은 회귀선입니다.

SST: 총 변동사항의 합(SSE+SST)로 y값들의 평균값과 실제 y값의 차이를 말합니다.

SSR: 분석을 통해서 설명이 가능해진 수치입니다.

SSE: 분석을 통해서 설명이 불가능한 수치입니다.



from sklearn.metrics import r2_score
r2 = r2_score(y, lr.predict(x_2)
Adjusted R-Squared

특징

- R2 Score의 문제점을 해결한다.

- 독립변수의 개수가 증가하면 일방적으로 증가하는 결정계수와 다르게 증가 시 분자를 감소시키는 연산을 통해서 일방적인 증가 방지합니다.

