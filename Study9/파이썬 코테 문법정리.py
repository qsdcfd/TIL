#!/usr/bin/env python
# coding: utf-8

# [집합 자료형]
# 2) 집합 자료형의 연산
#  i)합집합
#   | 이용한다
#  ii)교집합
#   & 이용한다
#  iii)차집합
#   - 이용한다
# 3)집합 자료형 관련 함수
#  i)add()함수: 하나의 집합 데이터에 값을 추가
#  ii)update()함수: 여러 개의 값을 한꺼번에 추가
#  iii)remove()함수: 특정값 제거
#  iv)시간 복잡도:O(1)
#  
# [조건문]
# :흐름 제어 문법
# 
# 1)비교 연산자
# X = Y :X와 Y가 서로 같을 때 참
# X != Y : X와 Y가 서로 다를 때 참
# X > Y : X가 Y보다 클 때 참
# X < Y : X가 Y보다 작을 때 참
# X >= Y: X가 Y보다 클 때 참
# X <= Y: X가 Y보다 작을 때 참
# 
# 2)논리 연산자
# X and Y : X와 Y가 모두 참일 때 참
# X or Y : X와 Y 중에 하나만 참이면 참
# not X : X가 거짓일 때 참이다
# 
# 3)파이썬의 기타 연산자
# X in 리스트: 리스트 안에 X가 들어가 있을 때 참
# X not in 문자열: 문자열 안에 X가 들어가 있지 않을 때참
# 
# [반복문]
# 
# 1)while문
# i) 조건문이 참 일때 한해서 반복적으로 코드 수행.
# ii)
# i = 0                     # 초기식
# while i < 100:            # while 조건식
#      print('Hello, world!')    # 반복할 코드
#      i += 1                    # 변화식
#      
# iii)  # 반복횟수 지정X(난수 이용)
# import random    # random 모듈을 가져옴
#  
# i = 0
# while i != 3:    # 3이 아닐 때 계속 반복
#     i = random.randint(1, 6)    # randint를 사용하여 1과 6 사이의 난수를 생성
#     print(i)
#      
# 2)for문
# i) in 뒤에 오는 데이터에 포함되어 있는 모든 원소를 첫 번째 인덱스부터 차례대로 하나씩 방문하고 in 뒤에 오는 데이터는 리스트, 튜플, 문자열 등이 될 수 있다.
# 
# ii)for 변수 in 리스트:
#        반복할 코드
# iii) for문 중첩 가능.
# iv) continue를 통해서 프로그램의 흐름을 반복문의 처음으로 돌아간다.
# 
# [함수]
# 
# 1)return: 함수에서 반환값 추출 담당
#    def add(a,b):
#        return a+b
#    print(add(3,7))
# 
# 2)return 없는 함수 구문
# 인자를 직접 지정하면 된다.
# 
# def add(a, b):
#     print('함수의 결과:' a+b)
# add(b =3, a = 7)
# 
# 3)global전역변수
# 함수 안에서 함수 밖의 변수 데이터 변경
# 지역 변수 선언 없이 바로 참조 가능.
# a = 0
# 
# def func():
#     global a
#     a += 1
# for i in range(10):
#     func()
#     
# print(a)
# 
# [입출력]
# 
# 1)입력
# i) 정수형 데이터 처리하는 int()함수 사용
# -> n = int(input()
# ii)입력받은 문자열을 띄어쓰기로 구분하여 각각 정수 자료형의 데이터로 저장하는 코드
# -> 변수명 = list(map(int,input().split()))
# iii)공백을 기준으로 구분하여 적은 수의 데이터 입력
# -> n,m,k = map(int,input().split())
# 
# iv) input()남발하면 시간 초과가 일어난다 고로
#    sys라이브러리에 정의되어 있는 sys.stdin.readline()함수 이용
#    
#    import sys
#    sys.stdin.readline().rstrip() # readline()사용하면
#    줄 바꿈 기호가 입력이 되는데 그 공백 문자를 없애주는 것이 rstrip()이므로 무조건 사용해야 한다
#    
# v)변수를 문자열로 바꾸어 출력하는 소스 코드
# answer = 7
# 
# print("정답은" + str(answer) + "입니다.")
# 
# vi)출력 줄 바꿈
# a = 1
# b = 2
# 
# print(a)
# print(b)
# 
# vii)각 변수를 콤마(,)로 구분하여 출력하는 소스코드
# answer = 7
# 
# print("정답은",str(answer),"입니다.")
# -->의도치 않은 공백 삽입 가능
# 
# [주요 라이브러리의 문법과 유의점]
# 
# 1)표준 라이브러리
# : 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현
# https://docs.python.org/ko/3/library/index.html
# 
# 1-1)예시
# i)내장함수: print(),input()입출력 기능~sorted()정렬 기능까지 포함.(without import명령어)
# sum()메서드 + iterabl객체 : 모든 원소의 합 반환
# min()메서드 + iterable객체: 모든 원소 중 최솟값 반환.
# max()메서드 + iterable객체: 모든 원소 중 최댓값 반환.
# sorted()메서드 + iterable객체: 정렬된 원소들을  결과값으로 반환(key속성으로 정렬 기준 명시 가능 ,
# reverse속성으로 정렬된 결과 리스트 뒤집기 가능)
#  +) sort()로도 정렬 가능.
# eval()메서드 + 문자열 형식: 해당 수식을 계산하여 결과 반환
# 
# result = eval("(3+5)* 7")
# print(result)
# 
# 
# ii)itertools:파이썬에서 반복되는 형태의 데이터를 처리하는 기능을 제공하는 라이브러리. 순열과 조합 제공.
# 
# - permutations: iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 모든 경우(순열) 계산. 클래스 이므로
# 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
# ex)
# from itertools import permutations
# 
# data = ['A', 'B', 'C'] # 데이터 준비
# result = list(permutations(data,3)) # 모든 순열 구하기
# 
# print(result)
# 
# 결과값은 나올 수 있는 여러 경우의 수가 나온다 (총 6가지)
# 
# - combinations: iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우(조합) 계산.
# ex)
# from itertools import combinations
# 
# data = ['A', 'B', 'C'] #데이터 준비
# result = list(combinations(data,2)) # 2개를 뽑는 모든 조합 구하기
# 
# print(result)
# 
# 결과값은 나올 수 있는 여러 경우의 수가 나온다 (총 3가지)
# 
# - product: iterable객체에서 r개의 데이터를 뽑아 일렬로 나열하는 순열 계산.
# 단, product객체는 초기화 할 때  뽑고자 하는 데이터의 수를 repeat속성 값으로 넣어줌. 
# 클래스 이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
# 
# ex) 리스트['A','B','C']에서 중복을 포함하여 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우의 수
# 
# from itertools import product
# 
# data = ['A', 'B', 'C'] # 데이터 준비
# result = list(product(data, repeat=2)) # 2개를 뽑는 모든 순열 구하기(중복 허용)
# 
# print(result)
# 결과값은 나올 수 있는 여러 경우의 수가 나온다 (총 9가지)
# 
# - combinations_with_replacement: iterable객체에서 r개의 데이터를 뽑아 순서를 고려하지 않고 나열하는 모든 경우의 수.(조합) 계산.
# 원소를 중복해서 뽑음. 
# 클래스 이므로 객체 초기화 이후에는 리스트 자료형으로 변환하여 사용
# 
# ex)리스트['A','B','C']에서 중복을 포함하여 2개(r=2)를 뽑아 순서에 상관없이 나열하는 모든 경우의 수
# 
# from itertools import combinations_with_replacement
# 
# data = ['A','B','C'] #데이터 준비
# result = list(combinations_with_replacement(data,2))
# #2개를 뽑는 모든 조합 구하기(중복,허용)
# 
# print(result)
# 
# 결과값은 나올 수 있는 여러 경우의 수가 나온다 ( 총6가지)
# 
# iii)heapq:힙(Heap)기능을 제공하는 라이브러리로 우선순위 큐 기능 구현
# -힙(heap)기능--> heapq라이브럴 제공하고 이는 다익스트라 최단경로 알고리즘을 포함하여 다양한 알고리즘에서
# 우선 순위 큐 기능 구현.
# 
# -파이썬의 힙은 최소 힙으로 구성되어 있어서 원소를 전부 넣었다 빼는 것만으로 시간복잡도 O(NlogN)에
# 오름차순 정렬 완료.
# -heapq.heappush()메서드: 힙에 원소 삽입
# -heappq.heappop()메서드: 힙에 원소 빼기
# - 힙 정렬 예제
# imporrt = heqpq
# 
# def heapsort(iterable):
#     h= []
#     result = []
#     #모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h,value)
#     #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
#     for i in range(len(h)):
#         result.append(heapq.heappop(h))
#     return result
#     
# result = heapsort([1,3,5,7,9,2,4,6,8,0])
# print(result)
# 
# [0,1,2.3,4,5,6,7,8,9]
# 
# -힙은 최대 힙을 제공하지 않으므로 heapq라이브러리를 이용하여 우너소의 부호를 임시 변경하여 사용.
# 힙에 원소를 삽입하기 전에 부호를 잠깐 바꾼 후, 원소를 꺼낸 뒤 다시 부호 변경.
# ex)
# 
# import heapq
# 
# def heapsort(iterable):
#     h =[]
#     result = []
#     #모든 원소를 차례대로 힙에 삽입
#     for value in iterable:
#         heapq.heappush(h, -value)
#     for i in range(len(h)):
#         result.append(-heapq.heappop(h))
#     return result
#     result = heapsort([1,3,5,7,9,2,4,6,8,0])
#     print(result)
#     
# [9,8,7,6,5,4,3,2,1,0]
# 
# 
# iv)bisect: 이진 탐색 기능 제공
# : 정렬된 배열에서 특정한 원소 찾기
# <시간 복잡도는 O(logN)
# - bisect_left(a, x): 정렬된 순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 왼쪽 인덱스 찾는 메서드,
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구할 때도 효과적.
# - bisect_right(a, x):정렬된 순서 유지하면서 리스트 a에 데이터 x를 삽입할 가장 오른쪽 인덱스 찾는 메서드
# 정렬된 리스트에서 값이 특정 범위에 속하는 원소의 개수 구할 때도 효과적.
# EX)
# from bisect import bisect_left, bisect_right
# 
# a = [1,2,4,4,8]
# x = 4
# 
# print(bisect_left(a,x)) # 2
# print(bisect_right(a,x))# 4
# 
# 
# EX2)
# 정렬된 리스트에서 값이 [left_value, right_value]에 속하는 데이터의 개수 반환. 원소의 값을 x라고 할 때,
# left_value <= x <= right_value인 원소의 개수를 O(logN)으로 빠르게 계산.
# from bisect import bisect_left, bisect_right
# 
# #값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
# def count_by_range(a, left_value, right_value):
#     right_index = bisect_right(a, right_value)
#     left_index = bisect_left(a, left_value)
#     return right_index - left index
#     
# #리스트 선언
# a = [1,2,3,3,3,3,4,4,8,9]
# 
# 
# #값이 4인 데이터 개수 출력
# print(count_by_range(a,4,4)) # 2
# 
# #값이 [-1,3] 범위에 있는 데이터 개수 출력
# print(count_by_range(a,-1,3)) # 6
# 
# v)collections: 덱(deque), 카운터(counter)등의 자료구조 포함
# :유용한 자료구조를 제공하는 표준 라이브러리.
# -deque:
# 이것을 통해서 큐를 구현함. 인덱싱, 슬라이싱등의 기능 사용할 수 없음 
# 허나, 연속적으로 나열된 데이터의 시작 부분이나 끝부분에 데이터 삽입하거나 삭제할 때 매우 효과적이고 
# 스택이나 큐의 기능을 모두 포함하기 때문에 스택 혹은 큐 자료구조의 대용으로 사용.
# 시간복잡도 :O(1)
# 
# -popleft():첫 번째 원소 제거.
# -pop(): 마지막 원소 제거
# -appendleft():첫 번째 인덱스에 원소 삽입
# -append():마지막 인덱스에 원소 삽입
# ---> 큐 자료구조 이용 때 사용되고, 항상 먼저 들어온 원소는 항상 먼저 나간다.
# ex)
# from collections import deque
# 
# data = deque([2,3,4])
# data.appendleft(1)
# data.append(5)
# 
# print(data)
# print(list(data)) #리스트 자료형으로 반환.
# 
# deque([1,2,3,4,5])
# [1,2,3,4,5]
# 
# -counter:
# 등장 횟수를 세는 기능 제공.
# iterable객체가 주어졌을 때, 해당 객ㅊ 내부의 원소가 몇 번씩 등장했는지 알려줌
# -> 원소별 등장 횟수를 세는 기능이 필요할 때 짧은 소스코드로 구현 가능
# ex)
# from collections import Counter
# 
# counter = Counter(['red','blue','red','green','blue','blue'])
# 
# print(counter['blue']) # 'blue'가 등장한 횟수 출력(3)
# print(counter['green']) # 'greeb'가 등장한 횟수 출력(1)
# print(dict(counter)) #사전 자료형 변환 {'red':2 , 'blue':3, 'green':1}
# 
# vi)match: 필수적인 수학적 기능 제공(팩토리얼, 제곱근, 최대공약수, 삼각함수 메서드~파이 상수)
# ex)
# import math
# 
# print(math.factorial(5)) # 5팩토리얼을 출력
# 
# ex2)
# import math
# 
# print(math.sqrt(7)) # 7의 제곱근을 출력
# 
# ex3)
# import math
# 
# print(math.gcd(21,14)) # 7
# 
# ex4)
# import math
# 
# print(math.pi) #파이(pi) 출력 3.141592653589793
# print(math.e) # 자연상수 e출력 2.718281828459045

# In[ ]:


zip함수는 (키,값)으로 되어도
결과는 키:값, 키:값 이렇게 해줌. 
* 시퀀스 객체 마지막 값 계산 *
 시퀀스 객체[len(시퀀스객체)-1]

