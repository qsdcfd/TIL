### 논문 DeepFM baseline

DeepFM: A Factorization-Machine based Neural Network for CTR Prediction
URL: [1703.04247] DeepFM: A Factorization-Machine based Neural Network for CTR Prediction (arxiv.org)

<br>

### Abstract

DeepFM은 CTR을 예측하는 모델이며 FM과 Deep Learning을 통합하여 feture들의 interaction 모델링한다. FM과 DL부분이 같은 inpute을 공유하기에 별도의 feature engineering 필요없다
feature interaction?
CTR을 정확하게 예측하기 위해서는, user의 클릭 로그로부터 feature interaction을 면밀히 파악하는 것이 중요하다. 아래는 다양한 상황으로부터 고려할 수 있는 interaction 예시다 .
•	사람들은 식사시간에 배달앱을 다운로드하는 경향이 있다.
→→ ‘app category’ 와 ‘time’ 간의 interaction 존재 (order-2)
•	10대 남자들은 rpg 게임을 선호한다.
→→ ‘app category’ 와 ‘gender’ 와 ‘age’ 간의 interaction 존재 (order-3)
•	사람들은 맥주와 기저귀를 함께 구매하는 경향이 있다.
→→ ‘beer’ 와 ‘diaper’ 간의 숨겨진 interaction 존재 (order-2)
위의 두 예시는 발견하기 쉽고 또 이해하기도 쉬운 반면, 마지막 예시는 모델이 자동으로 찾아주지 않으면 포착하기 어려운 interaction 일 수 있다. 따라서 CTR 예측모델을 고려할 때는, 명시적인 interaction과 숨겨진 interaction을 둘 다 잡아낼 수 있는 모델을 고려하는 것이 중요하다. (DeepFM이 두 파트로 구성된 이유)

<br>

### Previous studies
interaction을 고려하는 모델에는 아래와 같은 것들이 있으며, 각각 장단점이 존재한다.
•	Generalized Linear Model (GLM)
→→ 일반적으로 order-2 interaction까지만 고려하며 그 이상은 일반화 하기가 어렵다.
•	Factorization Machine (FM)
→→ low-order 뿐만 아니라 high-order interaction도 이론상으로 모델링 가능하다. 하지만 후자까지 고려할 경우 모델의 complexity가 너무 커져 사실상 사용하기 어렵다.
•	Factorization Machine supported Neural Network (FNN)
→→ NN 기반이므로 high-order interaction은 모델링 가능하다. 하지만 low-order를 제대로 포착하기 어렵고 pre-train FM 을 사용하기 때문에 이것의 성능이 모델 전체의 성능을 좌우하게 되는 단점이 있다.
•	Wide & Deep
→→ linear 모델 (wide part) 과 Neural Net 모델(deep part) 을 통합한 모델이다. low-order와 high-order interaction을 모두 포착할 수 있지만, wide 파트의 경우 고도의 feature engineering이 필요하다는 단점이 있다.

<br>

### Contribution
•	DeepFM은 low-order와 high-order feature interaction을 모두 포착할 수 있다. 비슷한 구조인 Wide & Deep 모델과 다르게 end-to-end 방식으로 학습되며 별도의 feature engineering이 필요 없다
 
 ![image](https://user-images.githubusercontent.com/86671456/188315682-4aa7d308-41f0-440e-b76c-1b4a632a05d2.png)

•	DeepFM은 FM 파트와 DL 파트가 input과 embedding 벡터를 공유하기 때문에 효율적인 학습이 가능하다.

