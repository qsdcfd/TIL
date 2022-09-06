# 기업이 어떻게 지식 그래프를 활용하여 추천을 하는가?

## 드라마앤컴퍼니 사례 보기(기술 블로그 정리)

### 주제: KGAT를 이용하여 인재 추천 시스템 연구 

<br>

### Intro

**추천시스템이란**

- 정의: 유저의 행동, 선호 등 유저르 파악할 수 있는 정보를 바탕으로, user-item간의 관계를 찾아서 선호 아이템을 예측

- 기업 사례: 유저의 행동과 로그 기반으로한 광고 추천시스템, 리쿠르터가 찾는 적합한 인재 추천

- 방식: 사용 가능하 데이터의 형태나 목적에 따라서 적합하 방법론을 선택하여 추천시스템을 만든다.

<br>

**Collaborative Filtering**

https://i0.wp.com/blog.dramancompany.com/wp-content/uploads/2022/06/그림1-1.png?w=1338&ssl=1![image](https://user-images.githubusercontent.com/86671456/188522219-22ed657a-167e-4394-be4b-bc5d652d7b60.png)

- 기본 개념
   - user1이 item 1,3,4 선호
   - user3이 item 3,4 선호
   - item 3을 user 1,3이 선호하면, user3 기준으로 동일하 아이템을 선호하는 사용자 user1이 선호하는 item1도 user3이 좋아하 것입니다.

<br>

**Content-based Filtering**

https://i0.wp.com/blog.dramancompany.com/wp-content/uploads/2022/06/그림2.png?w=1856&ssl=1![image](https://user-images.githubusercontent.com/86671456/188522511-3b86f05c-63f8-4170-8cf5-5647a06fc97f.png)

- 기본 개념
   - 정의: 유저가 특정 아이템을 선호할 경우 그 아이템과 비슷한 컨텐츠를 가지는 다른 아이템을 추천해주는 방법
   - 유저의 다른 정보, 특징으 제외학 오로지 아이템의 특징만으로 추천
   - 필수적으로 필요한 것: Item에 대한 특징, 정보 등의 데이터가 필요
   - user A는 Movie A를, user B & C는 Movie B르 선호합니다. 
   - 그러므로 user A는 Movie A를 선호하기에 유사한 장르인 Movie C도 선호한다.




