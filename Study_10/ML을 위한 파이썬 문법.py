#!/usr/bin/env python
# coding: utf-8

# [for]
# 
# 1)for 과 enumerate
# * enumerate는 순서와 리스트의 값을 함께 반환함.
# 
# my_list = ['a','b','c','d']
# 
# for i, value in enumerate(my_list):
#     print("순번 : ", i, " , 값 : ", value)
#     
# 2)이중 for문
# 
# my_list = ['a','b','c','d']
# result_list = []
# 
# for i in range(2):
#     for j in my_list:
#         result_list.append((i, j))
#         
# print(result_list)
# 
# 3)for-range
# 
# for i in range(100,1,-10):
#     print('i ==>{}', format(i))
#     
# 4)리스트 컴프리헨션(list Comprehension)
# 
# * 꼴 : 시퀀스 객체 결과 = [조건식 for1 for2]
# 
# my_list = ['a','b','c','d']
# 
# result_list = [(i, j) for i in range(2) for j in my_list]
# 
# print(result_list)
# 
# 5)제너레이터(generator)(데이터 양이 많을 때 사용)
# 
# my_list = ['a','b','c','d']
# 
# #인자로 받은 리스트로부터 데이터를 하나씩 가져오는 제너레이터를 리턴하는 함수
# def get_dataset_generator(my_list):
#     result_list = []
#     for i in range(2):
#         for j in my_list:
#             yield (i, j)   # 이 줄이 이전의 append 코드를 대체했습니다. 코드 실행의 순서를 밖으로 양보.
#             print('>>  1 data loaded..')
# 
# dataset_generator = get_dataset_generator(my_list)
# for X, y in dataset_generator:
#     print(X, y)
#     
# [Try - Except]
# : 에러를 잡기 위한 수 많은 노력.(에러 무시 or에러처리)
# https://d3s0tskafalll9.cloudfront.net/media/original_images/F-9-4.png
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
#     
# 6)Mutltiprocessing
# https://sebastianraschka.com/Articles/2014_multiprocessing.html
# 
# i)실행시간  측정
#  +)순차 처리
#  
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
#     print("finish : ", name) #finish : p1 
#                               finish : p2
#                               finish : p3
#                               finish : p4
# 
# for num in num_list:
#     count(num)
# 
# print("time :", time.time() - start)
# #time : 9.40987753868103
# 
#  +)병렬 처리
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
# if __name__ == '__main__': #코드의 시자점이 여기.
#     pool = multiprocessing.Pool(processes = 4)#4개프로세스 사용
#     pool.map(count, num_list)#병렬화를 시키는 함수로   count함수에 num_list원소를 하나씩 넣는다.
#     pool.close()#일반적으로 병렬화가 끝나면 나온다
#     pool.join()# 병렬처리 작업 끝날 때까지 기다림
# 
# print("time :", time.time() - start) 
# #time: 6.9532859325408936
# 
# #결과는 끝나는 순서대로 p값이 나온다. 순차처리 처럼
# p1,p2,p3,p4이렇게 나오지 않고 무작위로 나온다
# 
# 7)함수개념
# :수 많은 것을 반복할 때 효율적으로 쓰임
# ex)최댓값 구하기
# 
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
# 7-1) 이중 함수구문
# 
# def say_something(txt):
#     return txt
# 
# def send(function, count):
#     for i in range(count):  
#         print(function)
#     
# send(say_something("안녕!"), 2) #send(함수객체,객체)
# 
# 8)pass개념
# :기타 제어 흐름 도구로 에러난 곳을 넘어간다.
# 
# * try-except 대신 try-pass 가능한가?
# 
# 9)람다 표현식(lambda expression)
# :런 타임에 사용하는 익명 함수.
# https://wikidocs.net/64
# 
# lambda 인자: 표현식
# 
# 10)클래스(class)
# : 비슷한 애들끼리 모아둠
# 
# 11)모듈(Module)
# :함수, 변수, 클래스 모아 놓은 파일.
# 
# 12)패키지
# :여러 모듈을 하나로 모아둔 폴더
# https://pypi.org/
# 
# [프로그램 패러다임과 함수형 프로그래밍]
# 
# 1)절차 지향 프로그래밍.
# : 일이 진행되는 순서대로 함.
# 장점: 순차성으로 인해 읽기 편함
# 단점: 순차성 이기에 오류 생기면 도미노처럼 ..망함
# 
# 2)객체 지향 프로그래밍
# :객체 먼저 작성 후 함수 작성.
# 장점: 코드 재사용. 분석 쉽고 아키텍처 바꾸기 쉬움.
# 단점: 상호작용으로 인해 소요시간 많이 걸림.
# ex)파이썬
# http://schoolofweb.net/blog/posts/%ED%8C%8C%EC%9D%B4%EC%8D%AC-oop-part-1-%EA%B0%9D%EC%B2%B4-%EC%A7%80%ED%96%A5-%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8Doop%EC%9D%80-%EB%AC%B4%EC%97%87%EC%9D%B8%EA%B0%80-%EC%99%9C-%EC%82%AC%EC%9A%A9%ED%95%98%EB%8A%94%EA%B0%80/
# 
# 3)함수형 프로그래밍
# :데싸에게 필요. 효율성.버그 없는 코드. 병렬프로그래밍.
# :문제 분해.외부적으로 변동 없음
# 
# 3-1)순수성
# :내부 수정과 외부 수정이 없어 부작용이 전혀 없는 순수함수이다.(대입문 불가)
# 
# 3-2)모듈성
# 작은 조각으로 분해. 가독성이 좋고 오류 찾기 쉬움.
# 
# 3-3) 디버깅과 테스트 용이성
# https://docs.python.org/ko/3/howto/functional.html
# 
# [파이써닉하게 코드 짜기]
# 
# https://python-guide-kr.readthedocs.io/ko/latest/writing/style.html
# 
# https://pep8.org/#code-lay-out
# 
# 1)Whitespace
# -한 줄의 코드 길이가 79자 이하여야 합니다.
# -함수와 클래스는 다른 코드와 빈 줄 두 개로 구분합니다.
# -클래스에서 함수는 빈 줄 하나로 구분합니다.
# -변수 할당 앞뒤에 스페이스를 하나만 사용합니다.
# -리스트 인덱스, 함수 호출에는 스페이스를 사용하지 않습니다.
# -쉼표(,), 쌍점(:), 쌍반점(;) 앞에서는 스페이스를 사용하지 않습니다
# 
# 2)주석
# -코드의 내용과 일치하지 않는 주석은 피해야 합니다.
# -불필요한 주석은 피해야 합니다.
# 
# 3)이름 규칙
# -변수명 앞에 _(밑줄)이 붙으면 함수 등의 내부에서만 사 용되는 변수를 일컫습니다.
# 
# -변수명 뒤에 _(밑줄)이 붙으면 라이브러리 혹은 파이썬   기본 키워드와의 충돌을 피하고 싶을 때 사용합니다
# 
# -소문자 L, 대문자 O, 대문자 I를 가능하면 사용하지 마세요. 특정 폰트에서는 가독성이 굉장히 안 좋습니다.
# 
# -모듈(Module) 명은 짧은 소문자로 구성되며, 필요하다면 밑줄로 나눕니다.
# 
# -클래스 명은 파스칼 케이스(PascalCase) 컨벤션으로 작성합니다. 네이밍 컨벤션은 뒤에서 다시 설명하겠습니다.
# 
# -함수명은 소문자로 구성하되 필요하면 밑줄로 나눕니다.
# 
# -상수(Constant)는 모듈 단위에서만 정의하고 모든 단어는 대문자이며, 필요하다면 밑줄로 나눕니다.
# 
# 4)네이밍 컨벤션(Naming convention)
# : 혼동 및 업무 효율을 위한 통일성 갖추기.
# 
# +) snake_case
# 
# -모든 공백을 "_"로 바꾸고 모든 단어는 소문자입니다.
# -파이썬에서는 함수, 변수 등을 명명할 때 사용합니다.
# -ex) this_snake_case
# 
# +) PascalCase
# 
# -모든 단어가 대문자로 시작합니다.
# -UpperCamelCase, CapWords라고 불리기도 합니다.
# -파이썬에서는 클래스를 명명할 때 사용합니다.
# -ex) ThisPascalCase
# 
# +) camelCase
# 
# -처음은 소문자로 시작하고 이후의 모든 단어의 첫 글자는 대문자로 합니다.
# -lowerCamelCase라고 불리기도 합니다.
# -파이썬에서는 거의 사용하지 않습니다 (Java 등에서 사용)
# -ex) thisCamelCase

# In[1]:


# mycalculator.py

test = "you can use this module."

def add(a, b):
    return a + b
 
def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b


class all_calc():

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b
 
    def mul(self):
        return self.a * self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b


# In[2]:


code = '# mycalculator.py\ntest = "you can use this module."\n\ndef add(a, b):\n    return a + b\n \ndef mul(a, b):\n    return a * b\n\ndef sub(a, b):\n    return a - b\n\ndef div(a, b):\n    return a / b\n\n\nclass all_calc():\n\n    def __init__(self, a, b):\n        self.a = a\n        self.b = b\n\n    def add(self):\n        return self.a + self.b\n \n    def mul(self):\n        return self.a * self.b\n\n    def sub(self):\n        return self.a - self.b\n\n    def div(self):\n        return self.a / self.b'

f = open("mycalculator.py", "w")
f.write(code)
f.close()


# In[3]:


# import 모듈이름
import mycalculator


# In[4]:


# 모듈이름.함수이름()
print(mycalculator.add(4, 2))


# In[5]:


import mycalculator as mc

# 모듈이름.함수이름()
print(mc.add(4, 2))


# In[ ]:




