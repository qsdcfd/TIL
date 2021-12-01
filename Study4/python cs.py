#!/usr/bin/env python
# coding: utf-8

# 목차
# 
# 1파이썬 어디까지 써 봤니?!
# 
# 2파이썬을 더 잘 사용해보자!
# 
# 2.1 For문 잘 써보기
# 
# 2.2 Try - Except
# 
# 2.3 Multiprocessing
# 
# 3같은 코드 두 번 짜지 말자!
# 
# 3.1 함수(Function)
# 
# 3.2 람다 표현식
# 
# 3.3 클래스(Class), 모듈(Module), 패키지(Package)
# 
# 4프로그래밍 패러다임과 함수형 프로그래밍
# 
# 5파이써닉하게 코드를 짜보자!
# 

# In[1]:


import time
start = time.time()  # 시작 시간 저장

a = 1
for i in range(100):
	a += 1
 
# 작업 코드
print("time :", time.time() - start) # 결과는 '초' 단위 입니다.


# In[2]:


my_list = ['a','b','c','d']

for i in my_list:
    print("값 : ", i)


# In[3]:


my_list = ['a','b','c','d']

for i, value in enumerate(my_list): # enumerate()은 순서와 리스트의 값을 함께 반환
    print("순번 : ", i, " , 값 : ", value)


# In[5]:


my_list = ['a','b','c','d']
result_list = []

for i in range(3):
    for j in my_list:
        result_list.append((i, j))
        
print(result_list)


# In[8]:


my_list = ['a','b','c','d']
result_list = []

for i in list(range(1,10,2)):
    for j in my_list:
        result_list.append((i, j))
        
print(result_list)


# In[9]:


# 리스트 컴프리헨션(list Comprehension)
my_list = ['a','b','c','d']

result_list = [(i, j) for i in range(2) for j in my_list]

print(result_list)


# In[ ]:


#제너레이터(generator)
my_list = ['a','b','c','d']

# 인자로 받은 리스트를 가공해서 만든 데이터셋 리스트를 리턴하는 함수
def get_dataset_list(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            result_list.append((i, j))
    print('>>  {} data loaded..'.format(len(result_list)))
    return result_list

for X, y in get_dataset_list(my_list):
    print(X, y)


# In[ ]:


my_list = ['a','b','c','d']

# 인자로 받은 리스트로부터 데이터를 하나씩 가져오는 제너레이터를 리턴하는 함수
def get_dataset_generator(my_list):
    result_list = []
    for i in range(2):
        for j in my_list:
            yield (i, j)   # 이 줄이 이전의 append 코드를 대체했습니다
            print('>>  1 data loaded..')

dataset_generator = get_dataset_generator(my_list)
for X, y in dataset_generator:
    print(X, y)


# <예외 처리 방법>
# --> 코드 수행하다가 에러 발생 시 무시 혹은 처리.
# [Try - Except]
# 
# a = 10
# b = 0 
# 
# try:
#     #실행 코드
#     print(a/b)
# 		
# except:
#     print('에러가 발생했습니다.')
#     #에러가 발생했을 때 처리하는 코드
#     b = b+1
#     print("값 수정 : ", a/b)

# <Multiprocessing(멀티프로세싱)>
# https://sebastianraschka.com/Articles/2014_multiprocessing.html
# -parallel processing(병렬처리)
# 
# import multiprocessing
# import time
# 
# num_list = ['p1','p2', 'p3', 'p4']
# start = time.time()
# 
# def count(name):
#     for i in range(0, 100000000):
#         a = 1+2
#     print("finish : ", name)
#     
# 
# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes = 4)#병렬 처리시 4개의 프로세스 사용
#     pool.map(count, num_list)#병렬 시키는 함수로
#     count함수에 num_list원소 넣기
#     pool.close()#새로운 작업 추가하지 않을 때
#     pool.join() #프로세스가 종료될 때까지 대기
# 
# print("time :", time.time() - start)
# 
# 
# -serial processing(순차처리)
# 
# import time
# 
# num_list = ['p1','p2', 'p3', 'p4']
# start = time.time()
# 
# def count(name):
#     for i in range(0, 100000000):
#         a = 1 + 2
#         
#     print("finish : ", name)
# 
# for num in num_list:
#     count(num)
# 
# print("time :", time.time() - start)

# <같은 코드 두번 짜지 말자>
# * function(함수) 이용하기 *
# -->코드의 효율성. 재사용성.가독성 등을 좋게 해줌
# 
# def function_f(input_x):
# 	output_x = input_x * input_x
#     return output_x
# 
# ------------------------------------------------------
# 
# list_data = [10, 20, 30, 40]
# list_data2 = [20, 30, 40, 50]
# 
# length = len(list_data)
# max_result = list_data[0]
# for i in range(length):
#     if max_result < list_data[i]:
#         max_result = list_data[i]
#         
# print("최댓값은 ", max_result)
# 
# length = len(list_data2)
# max_result = list_data2[0]
# for i in range(length):
#     if max_result < list_data2[i]:
#         max_result = list_data2[i]
#         
# print("최댓값은 ", max_result)
# 
# 
# ------------------------------------------------------
# list_data = [10, 20, 30, 40]
# list_data2 = [20, 30, 40, 50]
# 
# def max_function(x):
#     length = len(x)
#     max_result = x[0]
#     for i in range(length):
#         if max_result < x[i]:
#             max_result = x[i]
#     return max_result
# 
# print("최댓값은 ", max_function(list_data))
# print("최댓값은 ", max_function(list_data2))
# 
# 
# * pass이용하기 *
# 
# pass는 기타 제어 흐름 도구로 아무것도 하지 않지만 특별히 할 일 없을 때 사용.
# 
# * 함수에 함수 사용 *
# 
# def say_something(txt):
#     return txt
# 
# def send(function, count):
#     for i in range(count):  
#         print(function)
#     
# send(say_something("안녕!"), 2)
# 
# * 함수 안의 함수 & 2개 이상의 return *
# 
# list_data = [30, 20, 30, 40]
# 
# def minmax_function(x_list):
#         
#     def inner_min_function(x):
#         length = len(x)
#         min_result = x[0]
#         for i in range(length):
#             if min_result > x[i]:
#                 min_result = x[i]
#         return min_result
#     
#     def inner_max_function(x):
#         length = len(x)
#         max_result = x[0]
#         for i in range(length):
#             if max_result < x[i]:
#                 max_result = x[i]
#         return max_result
#         
#     x_min = inner_min_function(x_list)
#     x_max = inner_max_function(x_list)
#     
#     minmax_list = [x_min, x_max]
# 
#     return minmax_list
# 
# print("최솟값, 최댓값은 : ", minmax_function(list_data))
# print("최솟값은 : ", minmax_function(list_data)[0])
# print("최댓값은 : ", minmax_function(list_data)[1])
# 
# 
# * 여러 변수로 변환하기 *
# list_data = [30, 20, 30, 40]
# 
# def minmax_function(x_list):
#         
#     def inner_min_function(x):
#         length = len(x)
#         min_result = x[0]
#         for i in range(length):
#             if min_result > x[i]:
#                 min_result = x[i]
#         return min_result
#     
#     def inner_max_function(x):
#         length = len(x)
#         max_result = x[0]
#         for i in range(length):
#             if max_result < x[i]:
#                 max_result = x[i]
#         return max_result
#         
#     x_min = inner_min_function(x_list)
#     x_max = inner_max_function(x_list)
#     
#     return x_min, x_max
# 
# min_value, max_value = minmax_function(list_data)
# 
# print("최솟값은 : ", min_value)
# print("최댓값은 : ", max_value)

# * 람다 표현식 *
# https://wikidocs.net/64
# --> 람다는 런타임에 생성해서 사용할 수 있는 익명 함수.
# (lambda 입력값받을 식: return부분)(입력값)
# 
# print( (lambda x,y: x + y)(10, 20) )
# 
# * map & lambda
# 
# result = list(map(lambda i: i * 2 , [1, 2, 3]))
# print(result)
# 
# * 클래스 *
# 
# 정의: 비슷한 역할을 하는 함수의 집합
# 
# * 모듈 *
# 
# 정의: 함수, 변수, 클래스를 모아 놓은 파일
# 
# * 패키지 *
# 
# 여러 모듈을 하나로 모아둔 폴더, 라이브러리이다.
# 
# 패키지는 pip을 이용해서 설치가 가능합니다.
# 
# https://pypi.org/
# 아래는 pypi에서 pandas를 검색해 나온 결과입니다. 사진 좌측 상단에서 볼 수 있듯이 pip install pandas 을 바로 복사하여 사용할 수 있습니다.

# <모듈 사용법>
# i)-->ii)-->iii)
# 
# i)mycalculator.py모듈 만들고 사칙연산 수행!
# 
# # mycalculator.py
# 
# test = "you can use this module."
# 
# def add(a, b):
#     return a + b
#  
# def mul(a, b):
#     return a * b
# 
# def sub(a, b):
#     return a - b
# 
# def div(a, b):
#     return a / b
# 
# 
# class all_calc():
# 
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
# 
#     def add(self):
#         return self.a + self.b
#  
#     def mul(self):
#         return self.a * self.b
# 
#     def sub(self):
#         return self.a - self.b
# 
#     def div(self):
#         return self.a / self.b
#         
# ii)
# 
# # import 모듈이름
# import mycalculator
# 
# iii)
# # 모듈이름.함수이름()
# print(mycalculator.add(4, 2))

# In[ ]:


< 패러다임 >
어떤 한 시대의 사람들의 견해나 사고를 근본적으로 
규정하고 있는 테두리이자 이론적인 틀 혹은 체계.

[ 프로그래밍]

1) 절차 지향 프로그래밍
 정의: 일이 순차적으로 진행됨
 장점: 읽기 편함
 단점: 혹시 위의 코드가 잘못되면 연쇄성으로 문제가 생겨
     유지 보수가 어렵고 코드가 길어져 분석이 힘들다
http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-1-%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8Doop%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EC%99%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80/
2) 객체 지향 프로그래밍(python)
  정의: 객체간의 상호작용이 되도록 개발자가 설정
  장점: 코드 재사용이 쉬워 분석이 쉽고 당연히
        아키텍처를 바꾸기 쉬움
  단점: 객체간의 상호작용으로 인해 설계에 많은 시간 소요
        설계 잘못되며ㅕㄴ 전체 바꿈
        
3)함수형 프로그래밍의 특징
https://docs.python.org/ko/3/howto/functional.html
 i)순수성
    부작용이 전혀 없는 함수.(변수를 변경시키는 코드X)
    A = 5

def impure_mul(b):
    return b * A

print(impure_mul(6))

함수 안에 함수 밖에서 바로 가져오는 함수나 아니면 
밖에 있는 변수를 변경시키는 코드가 없습니다. 
순수하게 함수 input 2개만을 이용해서 결과를 내보냅니다.
 
  ii)모듈성
   작은 조각으로 분해함-->가독성이 좋구 오류 확인 easy
    
    iii) 디버깅과 테스트 용이성
    모듈성과 입출력 예상 가능성으로인해 디버깅이 쉽고
    각 함ㅅ는 단위 테스트 대상으로 테스트가 쉽다.
    이유는 과거의 예상과 맞는지만 확인하면 되기때문.


# In[ ]:


Whitespace

i)한 줄의 코드 길이가 79자 이하여야 합니다.
y = a + a + a + a # 79자 이하
함수와 클래스는 다른 코드와 빈 줄 두 개로 구분합니다.
class a():
    pass
# 빈 줄
# 빈 줄
class b():
    pass
# 빈 줄
# 빈 줄
def c():
    pass
# 빈 줄
# 빈 줄
클래스에서 함수는 빈 줄 하나로 구분합니다.
class a():
	
	def b():
		pass
	
	def c():
		pass
ii)변수 할당 앞뒤에 스페이스를 하나만 사용합니다.
y = 1

iii)리스트 인덱스, 함수 호출에는 스페이스를 
사용하지 않습니다.
my_list = [1, 2, 3]
my_list[0] # 리스트 인덱스 호출

my_function(0) # 함수 호출

iv)쉼표(,), 쌍점(:), 쌍반점(;) 앞에서는 스페이스를 
사용하지 않습니다.
my_list = [1, 2, 3]; my_list[0:1]
if len(my_list) == 3: print my_list

  V)  주석
코드의 내용과 일치하지 않는 주석은 피해야 합니다.
불필요한 주석은 피해야 합니다.

  
    vi)이름 규칙
1)
변수명 앞에 _(밑줄)이 붙으면 함수 등의 내부에서만
사용되는 변수를 일컫습니다.


2)

_my_list = []
변수명 뒤에 _(밑줄)이 붙으면 라이브러리 혹은 파이썬 
기본 키워드와의 충돌을 피하고 싶을 때 사용합니다.

3)
import_ = "not_import"
소문자 L, 대문자 O, 대문자 I를 가능하면 사용하지 마세요. 특정 폰트에서는 가독성이 굉장히 안 좋습니다.
모듈(Module) 명은 짧은 소문자로 구성되며, 필요하다면 밑줄로 나눕니다.

4)
my_module.py
클래스 명은 파스칼 케이스(PascalCase) 컨벤션으로 작성합니다. 네이밍 컨벤션은 뒤에서 다시 설명하겠습니다.

5)
class MyClass():
	pass
함수명은 소문자로 구성하되 필요하면 밑줄로 나눕니다.
6)

def my_function():
	pass
상수(Constant)는 모듈 단위에서만 정의하고 
모든 단어는 대문자이며, 필요하다면 밑줄로 나눕니다.

7)

MY_PI = 3.14 # 상수는 변하지 않는 변수입니다.


-------
<네이밍 컨벤션(Naming convention)>
실무에선 다른 사람들과 같이 코드를 짜야 하는 경우가 
많습니다. 사람들마다 변수명을 적는 방식이 다르면 
코드가 깔끔해보이지 않기 때문에 가독성이 안 좋습니다. 
가독성이 좋은 코드를 짜는 방법은 통일성을 갖는 것입니다. 통일성을 갖기 위해선 사람들이 공유하는 코딩 스타일 가이드가 필요합니다. 그래서 파이썬에서는 pep8 이라는 코딩 스타일 가이드를 가지고 있습니다. pep8 코딩 스타일 가이드는 위에서 소개했기 때문에 이번엔 이름을 작성할 때 사용하는 네이밍 컨벤션에 대해서 알아보겠습니다.

대표적인 네이밍 컨벤션은 snake_case, 
PascalCase, camelCase 입니다. 각 네이밍 컨벤션의 기준에 
맞춰 코드를 작성하시면 가독성이 높은 코드가 됩니다.

1)snake_case

모든 공백을 "_"로 바꾸고 모든 단어는 소문자입니다.
파이썬에서는 함수, 변수 등을 명명할 때 사용합니다.
ex) this_snake_case
PascalCase

2)

모든 단어가 대문자로 시작합니다.
UpperCamelCase, CapWords라고 불리기도 합니다.
파이썬에서는 클래스를 명명할 때 사용합니다.
ex) ThisPascalCase
camelCase

3)

처음은 소문자로 시작하고 이후의
모든 단어의 첫 글자는 대문자로 합니다.
lowerCamelCase라고 불리기도 합니다.
파이썬에서는 거의 사용하지 않습니다 (Java 등에서 사용)

ex)thisCamelCase


# In[ ]:


python 참고 자료
https://python-guide-kr.readthedocs.io/ko/latest/writing/style.html

    https://pep8.org/#code-lay-out

