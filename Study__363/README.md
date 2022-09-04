### Introduction

<Goal>
  
CTR 예측이란, 아래 그림처럼 user에게 추천 아이템들이 주어졌을 때 user가 해당 아이템을 클릭할 확률을 추정하는 것이다. 이때 추정된 확률을 바탕으로, user의 선호 아이템 순위를 메길 수 있다.

Recommended items	Click through rate	Rank
Item7	0.3	5
Item19	0.8	2
Item12	0.4	4
Item86	0.6	3
Item11	0.9	1
Item12	0.1	6

Our Approach
아래는 DeepFM의 데이터 구조다. 총 nn개의 데이터가 있다고 할 때, 각 row는 user와 item 정보를 담고 있는 xx와 특정 아이템 클릭여부를 나타내는 yy 로 이루어져 있다.
 
x=[xfield1,xfield2,...,,xfieldj,...,xfieldm](1×d)
y∈{0,1}x=[xfield1,xfield2,...,,xfieldj,...,xfieldm](1×d)y∈{0,1}
먼저 x는 m개의 필드로 이뤄져 있으며 각 필드는 다양한 정보를 담고있다. 예를들어 user 필드에는 user의 id, 성별, 나이 등의 정보가, item 필드에는 특정 item의 구매 정보 등이 포함된다. 
각 필드에는 카테고리 피처일 경우 one-hot 벡터로, 연속적인 피처일 경우 해당 값을 그대로 사용할 수 있다. 일반적으로 xx는 굉장히 sparse 하며 고차원이다.

이어 y 는 user의 특정 item에 대한 클릭여부를 나타낸다. 
만약 user가 특정 item을 클릭 했을 경우 y=1, 클릭하지 않았을 경우 y=0이 된다.
위와 같은 데이터 구조를 고려할 때, DeepFM의 목표는 x 가 주어졌을 때, user가 특정 item을 클릭할 확률을 예측하는 것이 되겠다.
y^=CTR_model(x)=DeepFM(x)
