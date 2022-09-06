
### Recommendation based Knowledge Graph

**GNN**

- 귀납식 임베딩으로 연결 관계와 neighborhood noed들의 상태르 이용하여 각 node 상태르 업데이트하여 Node들으 벡터로 표현
- 그래프를 표현하는 node들을 임베딩하기 위한 하 noed에 대한 neighborhood node들의 정보, 상태를 aggregation하는 과정을 거쳐서 모델에 적용
- graph는 node-edge의 연결 구조이기에 edge를 통해서 node간의 관계를 파악하여 user-item간 관계등의 구조르 표현

<br>

**Knowledge Graph**

https://i0.wp.com/blog.dramancompany.com/wp-content/uploads/2022/06/스크린샷-2022-06-15-오전-11.24.36.png?w=1396&ssl=1![image](https://user-images.githubusercontent.com/86671456/188524376-aa4b35aa-c45f-47ba-9d31-a83a520f8fe3.png)

- 지식(Knowledge): 서로 관계가 있는 대상(entity)들 사이의 관계(relation)르 모아 놓은 것
- Knoledge Graph: Knowledge를 그래프의 구조로 표현한 것
- entity,relation = node, edge
- 구조 설명
   - relation이 triple 구조(head entity, relation, tail entity)의 형태로 표현되어서 head와 tail간의 특저 관계 암시
   - 예시: 소크라테스는 플라톤에게 영향으 주었다(socartes, influenced, plato)
- 그래프 표현 장점
   - 대상 간의 관계와 의미를 구조적으로 표현
   - 지시 그래프를 임베딩화하여 추천시스템에 적용하면, user or item 의 side information 포함
   - 각 entity별로 많은 표현력을 가질 수 있어서 추천 시스템의 성능 향사 기여

<br>

**Recommendation and Knowledge Graph**

