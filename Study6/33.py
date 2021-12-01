#!/usr/bin/env python
# coding: utf-8

# <Unit 클로저>
# 
# 1) 변수의 사용 범위 알아보기
# 
# * 전역 변수: 전체에 접근할 수 있는 변수
# 
# 
# x = 10          # 전역 변수
# def foo():
#     print(x)    # 전역 변수 출력
#  
# foo()
# print(x)        # 전역 변수 출력
# 
# * 지역변수: 특정 함수 내에서 만들어짐
# 
# def foo():
#     x = 10      # foo의 지역 변수
#     print(x)    # foo의 지역 변수 출력
#  
# foo()
# print(x)        # 에러. foo의 지역 변수는 출력할 수 없음
# 
# 2)함수 안에서 전역 변수 변경하기
#  global 전역변수
#  
# x = 10          # 전역 변수
# def foo():
#     global x    # 전역 변수 x를 사용하겠다고 설정
#     x = 20      # x는 전역 변수
#     print(x)    # 전역 변수 출력
#  
# foo()
# print(x)        # 전역 변수 출력 x = 10          # 전역 변수
# 
# #전역 변수 x가 없는 상태
# def foo():
#     global x    # 전역 변수 x를 사용하겠다고 설정
#     x = 20      # x는 전역 변수
#     print(x)    # 전역 변수 출력
#  
# foo()
# print(x)        # 전역 변수 출력
# 
# 3)함수 안에서 함수 만들기
# def 함수이름1():
#     코드
#     def 함수이름2():
#         코드
#         
#  ex)
# def print_hello():
#     hello = 'Hello, world!'
#     def print_message():
#         print(hello)
#     print_message() #바깥쪽 함수의 지역 변수를 사용
#  
# print_hello()
# 
# https://dojang.io/pluginfile.php/13867/mod_page/content/3/033003.png
# 
# 4)지역 변수 변경하기
# 
# +) nonlocal 지역변수
# 
# * 안쪽 함수에서 바깥쪽 함수의 지역변수 변경
# def A():
#     x = 10        # A의 지역 변수 x
#     def B():
#         nonlocal x    # 현재 함수의 바깥쪽에 있는 지역 변수 사용
#         x = 20        # A의 지역 변수 x에 20 할당
#  
#     B()
#     print(x)      # A의 지역 변수 x 출력
#  
# A()
# 
# 5)nonlocal이 변수를 찾는 순서
# 
# nonlocal: 현재 함수의 바깥쪽에 있는 지역변수를 찾을 때
# 가장 가까운 함수부터 먼저 찾는다.
# 
# def A():
#     x = 10
#     y = 100
#     def B():
#         x = 20
#         def C():
#             nonlocal x
#             nonlocal y
#             x = x + 30
#             y = y + 300
#             print(x)
#             print(y)
#         C()
#     B()
#  
# A()
# 
# 6)global로 전역 변수 사용하기
# x = 1
# def A():
#     x = 10
#     def B():
#         x = 20
#         def C():
#             global x
#             x = x + 30
#             print(x)
#         C()
#     B()
# A()
# 
# 
# 7)클로저 사용하기
# def calc():
#     a = 3
#     b = 5
#     def mul_add(x):
#         return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
#     return mul_add          # mul_add 함수를 반환
#  
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))
# 
# 8)lambda로 클로저 만들기
# def calc():
#     a = 3
#     b = 5
#     return lambda x: a * x + b    # 람다 표현식을 반환
#  
# c = calc()
# print(c(1), c(2), c(3), c(4), c(5))
# 
# 9)클로저의 지역변수 변경하기
# def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
#  
# c = calc()
# c(1)
# c(2)
# c(3)

# 참고 | 네임스페이스
# 파이썬에서 변수는 네임스페이스(namespace, 이름공간)에 저장됩니다. 다음과 같이 locals 함수를 사용하면 현재 네임스페이스를 딕셔너리 형태로 출력할 수 있습니다.
# 
# >>> x = 10
# >>> locals()
# {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, 'x': 10}
# 
# 출력된 네임스페이스를 보면 'x': 10처럼 변수 x와 값 10이 저장되어 있습니다. 여기서는 전역 범위에서 네임스페이스를 출력했으므로 전역 네임스페이스를 가져옵니다.
# 
# 마찬가지로 함수 안에서 locals를 사용할 수도 있습니다.
# 
# >>> def foo():
# ...     x = 10
# ...     print(locals())
# ...
# >>> foo()
# {'x': 10}
# 네임스페이스를 보면 'x': 10만 저장되어 있습니다. 이때는 지역 범위에서 네임스페이스를 출력했으므로 지역 네임스페이스를 가져옵니다.def calc():
#     a = 3
#     b = 5
#     total = 0
#     def mul_add(x):
#         nonlocal total
#         total = total + a * x + b
#         print(total)
#     return mul_add
#  
# 

# In[7]:


def A():
    x = 10        # A의 지역 변수 x
    def B():
        x = 20    # x에 20 할당
 
    B()
    print(x)      # A의 지역 변수 x 출력
A()


# In[ ]:


i=n+1
def count():
    nonlocal i
    i-=1 
    return i
return count


# In[ ]:


def count():
  nonlocal n
  r = n
  n -= 1
  return r
return count


# In[ ]:




