### KGAT : Knowledge Graph Attention Network

- 모델: graph 기반의 추천시스템에서 Knowledge graph와 Attention 메커니즘을 적용시키 모델

https://i0.wp.com/blog.dramancompany.com/wp-content/uploads/2022/06/그림4.png?w=938&ssl=1![image](https://user-images.githubusercontent.com/86671456/188525719-b88a9200-b978-4069-9f8a-ca4927489952.png)

- 효과
   - 현재 CF는 많은 산업에서 사용이 되지만 user's feature, context등의 부가적인 정보를 모델링하 수 없는 단점이 존재합니다.
   - CF + KG를 적용하여 해결
   - 위의 그리음 CKG를 의미하고, user-item 간의 edge가 존재하고, item에 대한 entity들이 KG로 표현이 됩니다.
   - 즉, KG와 user-item Graph와의 하이브리드 구조를 갖고 이름 CKG

<br>

**Methodology**

https://i0.wp.com/blog.dramancompany.com/wp-content/uploads/2022/06/그림5.png?w=1864&ssl=1![image](https://user-images.githubusercontent.com/86671456/188526046-3c4b60d1-409d-4bd7-95f8-f15575e23a63.png)

