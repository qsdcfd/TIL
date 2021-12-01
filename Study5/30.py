#!/usr/bin/env python
# coding: utf-8

#  <함수에서 위치 인수와 키워드 인수 사용하기>
#  
#  1) 위치 인수와 리스트 언패킹 사용
#     
#     i)위치인수(순서 대로 넣는 방식,즉.순서 정해져있음)
#     >>> print(10, 20, 30)
#       10 20 30
#       
#       [위치 인수 함수]
#       
#     >>> def print_numbers(a, b, c):
# ...     print(a)
# ...     print(b)
# ...     print(c)
# ...  
# 
#     ii)언패킹 사용하기(포장 풀기)
#     https://dojang.io/pluginfile.php/13788/mod_page/content/2/030001.png
#    
#    함수(* 리스트)
#    함수(* 튜플)
#    
# >>> x = [10, 20, 30]
# >>> print_numbers(*x)
# 10
# 20
# 30
# 
# >>> print_numbers(*[10, 20, 30])
# 10
# 20
# 30
# 
# 2)가변 인수 함수 만들기(인수의 개수가 정해짐X)
#   (With 위치 인수 와 리스트 언패킹)
# 
# def 함수이름(*매개변수):
#     코드  
#   
# >>> def print_numbers(*args):
# ...     for arg in args:
# ...         print(arg)
# ...
# 
# 
# >>> print_numbers(10)
# 10
# >>> print_numbers(10, 20, 30, 40)
# 10
# 20
# 30
# 40
# 
# ->넣은 숫자 만큼 출력.
# 
# >>> x = [10]
# >>> print_numbers(*x)
# 10
# >>> y = [10, 20, 30, 40]
# >>> print_numbers(*y)
# 10
# 20
# 30
# 40
# 
# 
# 3)키워드 인수 사용하기
# --> 매번 순서와 용도 기억할 필요 없어서 좋음
# * 함수(키워드=값)
# 
# >>> personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동
# 
# 4)키워드 인수와 딕셔너리 언패킹 사용하기
# 함수(**딕셔너리)
# --> 키-값쌍으로 저장되었기 때문에 ** 두 번 씀
# >>> def personal_info(name, age, address):
# ...     print('이름: ', name)
# ...     print('나이: ', age)
# ...     print('주소: ', address)
# >>> x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
# >>> personal_info(**x)
# 
# 
# https://dojang.io/pluginfile.php/13790/mod_page/content/2/030002.png
# 
# >>> personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동
# 
# 5)키워드 인수를 사용하는 가변 인수 함수 만들기
# i)특정 키가 있는지 확인
# def personal_info(**kwargs):
#     if 'name' in kwargs:    # in으로 딕셔너리 안에 특정 키가 있는지 확인
#         print('이름: ', kwargs['name'])
#     if 'age' in kwargs:
#         print('나이: ', kwargs['age'])
#     if 'address' in kwargs:
#         print('주소: ', kwargs['address'])
#         
# ii)형식 쓰기
# def 함수이름(**매개변수):
#     코드
# >>> def personal_info(**kwargs):
# ...     for kw, arg in kwargs.items():
# ...         print(kw, ': ', arg, sep='')
# ...    
# 
# 6)매개변수에 초깃값 지정하기
# def 함수이름(매개변수=값):
#     코드
#     
# >>> def personal_info(name, age, address='비공개'):
# ...     print('이름: ', name)
# ...     print('나이: ', age)
# ...     print('주소: ', address)
# ...
# 
# >>> personal_info('홍길동', 30)
# 이름:  홍길동
# 나이:  30
# 주소:  비공개
# 
# >>> personal_info('홍길동', 30, '서울시 용산구 이촌동')
# 이름:  홍길동
# 나이:  30
# 주소:  서울시 용산구 이촌동
# 
# 7)초기값이 지정된 매개변수의 위치
#  * 초기값이 지정된 매개변수 다음에는 초깃값이 없는 
#  매개변수가 올 수 없다.
#  
#  즉, 다음과 같이 초깃값이 지정된 매개변수는 뒤쪽에 몰아주면 됩니다.
# 
# def personal_info(name, age, address='비공개'):
# def personal_info(name, age=0, address='비공개'):
# def personal_info(name='비공개', age=0, address='비공개'):

# In[ ]:


참고 | 고정 인수와 가변 인수를 함께 사용하기
고정 인수와 가변 인수를 함께 사용할 때는 
다음과 같이 고정 매개변수를 먼저 지정하고, 
그 다음 매개변수에 *를 붙여주면 됩니다.

>>> def print_numbers(a, *args):
...     print(a)
...     print(args)
...
>>> print_numbers(1)
1
()
>>> print_numbers(1, 10, 20)
1
(10, 20)
>>> print_numbers(*[10, 20, 30])
10
(20, 30)
단, 이때 def print_numbers(*args, a):처럼 *args가 
    고정 매개변수보다 앞쪽에 오면 안 됩니다. 
    매개변수 순서에서 *args는 반드시 
    가장 뒤쪽에 와야 합니다.


# In[ ]:


참고 | 고정 인수와 가변 인수(키워드 인수)를 함께 사용하기
고정 인수와 가변 인수(키워드 인수)를 함께 사용할 때는 
다음과 같이 고정 매개변수를 먼저 지정하고, 
그 다음 매개변수에 **를 붙여주면 됩니다.

>>> def personal_info(name, **kwargs):
...     print(name)
...     print(kwargs)
...
>>> personal_info('홍길동')
홍길동
{}
>>> personal_info('홍길동', age=30, address='서울시 용산구 이촌동')
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}
>>> personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
홍길동
{'age': 30, 'address': '서울시 용산구 이촌동'}
단, 이때 def personal_info(**kwargs, name):처럼 
    **kwargs가 고정 매개변수보다 앞쪽에 오면 안 됩니다
    매개변수 순서에서 **kwargs는 반드시 
    가장 뒤쪽에 와야 합니다.


# In[ ]:


참고 | 위치 인수와 키워드 인수를 함께 사용하기
함수에서 위치 인수를 받는 *args와 키워드 인수를 받는 **kwargs를 함께 사용할 수도 있습니다. 대표적인 함수가 print인데 
print는 출력할 값을 위치 인수로 넣고 
sep, end 등을 키워드 인수로 넣습니다. 
다음과 같이 함수의 매개변수를 *args, **kwargs로 
지정하면 위치 인수와 키워드 인수를 함께 사용합니다.

>>> def custom_print(*args, **kwargs):
...     print(*args, **kwargs)
...
>>> custom_print(1, 2, 3, sep=':', end='')
1:2:3
단, 이때 def custom_print(**kwargs, *args):처럼 
    **kwargs가 *args보다 앞쪽에 오면 안 됩니다. 
    매개변수 순서에서 **kwargs는 
    반드시 가장 뒤쪽에 와야 합니다.

특히 고정 매개변수와 *args, **kwargs를 
함께 사용한다면
def custom_print(a, b, *args, **kwargs):처럼 
    매개변수는 고정 매개변수, *args, **kwargs 순으로
    지정해야 합니다.


# In[ ]:


def get_min_max_score(*args):
    return min(args), max(args)
def get_average(**kwargs):
    return sum((kwargs.values())/len(kwargs))

