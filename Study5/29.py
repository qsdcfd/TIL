#!/usr/bin/env python
# coding: utf-8

# <함수의 실행순서>
# 1.파이썬 스크립트 최초 실행
# 2.hello 함수 호출
# 3.hello 함수 실행
# 4.print 함수 실행 및 'Hello, world!' 출력
# 5.hello 함수 종료
# 6.파이썬 스크립트 종료
# 
# 
# <함수 호출>
# 
# def 함수이름():
#      코드
#           
# def hello():
#     print('Hello,world!')
# hello()
# 
# https://dojang.io/pluginfile.php/13778/mod_page/content/5/029001.
# 
# <함수 덧셈>
# def 함수이름(매개변수1, 매개변수2):
#     코드
#     
# >>> def add(a, b):
# ...     print(a + b)
#     add(a,b)
#     
#     
# a+b
# 
# 
# 
# 
# def add(a, b):
#     """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
#     return a + b
#  
# x = add(10, 20)       # 함수를 호출해도 독스트링은 출력되지 않음
# print(x)
#  
# print(add.__doc__)    # 함수의 __doc__로 독스트링 출력
# 실행 결과
# 30
# 이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다.
# 
# 
# <함수 반환>
# https://dojang.io/pluginfile.php/13780/mod_page/content/2/029003.png
# return:함수 바깥으로 값을 반환, 값을 변수에 저장
#     
# def 함수이름(매개변수):
#     return 반환값   
# 
# >>> def add(a, b):
# ...     return a + b
# >>> x = add(10, 20)
# >>> x
# 30
# 
# 
# 
# >>> def add(a, b):
# ...     return a + b
# >>> print(add(10, 20))
# 30
# 
# 
# <함수에서 값을 여러 개 반환>
# def 함수이름(매개변수):
#     return 반환값1, 반환값2
#     
# >>> def add_sub(a, b):
# ...     return a + b, a - b
# >>> x, y = add_sub(10, 20)
# >>> x
# 30
# >>> y
# -10
# https://dojang.io/pluginfile.php/13781/mod_page/content/2/029004.png
# 
# <함수 호출 과정>
# def mul(a, b):
#     c = a * b
#     return c
#  
# def add(a, b):
#     c = a + b
#     print(c)
#     d = mul(a, b)
#     print(d)
#  
# x = 10
# y = 20
# add(x, y)
# 
# https://dojang.io/pluginfile.php/13783/mod_page/content/4/029005.png
# 
# 전역프레임: 파일 실행이 끝나면 사라짐, 전체 접근
# 스택프레임: 값들

# In[ ]:


참고 | 빈 함수 만들기
내용이 없는 빈 함수를 만들 때는 코드 부분에 pass를 넣어줍니다.

def hello():
    pass
나중에 다른 사람이 만든 파이썬 소스 코드를 보다 보면 
pass를 자주 접할 수 있습니다.
pass는 아무 일을 하지 않아도 함수의 틀을 
유지할 필요가 있을 때 사용합니다.


# In[ ]:


참고 | 함수 독스트링 사용하기
파이썬에서는 함수의 :(콜론) 바로 
    다음 줄에 """ """(큰따옴표 세 개)로 
    문자열을 입력하면 함수에 대한 
    설명을 넣을 수 있습니다. 
    이런 방식의 문자열을 
    독스트링(문서화 문자열, documentation strings, docstrings)이라고 합니다. 
    단, 독스트링의 윗줄에 다른 코드가 오면 안 됩니다.

def 함수이름(매개변수):
    """독스트링"""
    코드
 
def 함수이름(매개변수):
    """
    여러 줄로 된 
    독스트링
    """
    코드
    
독스트링은 ' '(작은따옴표), " "(큰따옴표),
''' '''(작은따옴표 세 개)로 만들어도 되지만, 
파이썬 코딩 스타일 가이드(PEP 8)에서는 
""" """(큰따옴표 세 개)를 권장합니다.

앞에서 만든 add 함수에 독스트링으로 설명을 
추가해보겠습니다.


def add(a, b):
    """이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다."""
    return a + b
 
x = add(10, 20)       # 함수를 호출해도 독스트링은 출력되지 않음
print(x)
 
print(add.__doc__)    # 함수의 __doc__로 독스트링 출력
실행 결과
30
이 함수는 a와 b를 더한 뒤 결과를 반환하는 함수입니다.


# In[ ]:


참고 | 매개변수는 없고 반환값만 있는 함수
함수를 만들 때 매개변수는 없지만 값만 반환하는 함수를 만들 수도 있습니다. 다음은 매개변수 없이 1만 반환합니다.

>>> def one():
...     return 1
...
>>> x = one()
>>> x
1


# In[ ]:


참고 | return으로 함수 중간에서 빠져나오기
return은 값을 반환하는 기능뿐만 아니라 함수 중간에서
바로 빠져나오는 기능도 있습니다. 
다음은 매개변수 a가 10이면 함수를 그냥 빠져나옵니다.

>>> def not_ten(a):
...     if a == 10:
...         return
...     print(a, '입니다.', sep='')
...
>>> not_ten(5)
5입니다.
>>> not_ten(10)
>>> 
not_ten 함수에 5를 넣으면 print로 '5입니다.'를 
출력하지만, 10을 넣으면 return으로 
함수 중간에서 바로 빠져나오므로 
그 아래에 있는 print는 실행하지 않습니다. 

따라서 아무것도 출력되지 않습니다.

이처럼 return은 함수 중간에서 빠져나올 때
자주 사용합니다. 보통은 if와 조합해서 특정 조건일 때 
함수 중간에서 빠져나옵니다.


# 참고 | 값 여러 개를 직접 반환하기
# 함수에서 값 여러 개를 직접 반환할 때는 다음과 같이 return에 튜플을 지정해주면 됩니다.
# 
# def one_two():
#     return (1, 2)
# 사실 파이썬에서는 괄호 없이 값을 콤마로 구분하면 튜플이 되죠? 즉, 튜플 1, 2는 튜플 (1, 2)와 같습니다.
# 
# >>> 1, 2
# (1, 2)
# 따라서 return 1, 2는 return (1, 2)와 의미가 같습니다.
# 
# def one_two():
#     return 1, 2    # return (1, 2)와 같음
# 물론 return에서 리스트를 직접 반환해도 됩니다. 이때도 반환값을 변수 여러 개에 저장할 수 있습니다.
# 
# >>> def one_two():
# ...     return [1, 2]
# ...
# >>> x, y = one_two()
# >>> print(x, y)
# 1 2

# In[16]:


x, y = map(int, input().split())
def calc(a,b):
    return a+b,a-b,a*b,a/b

a, s, m, d = calc(x, y)
print('덧셈: {0}, 뺄셈: {1}, 곱셈: {2}, 나눗셈: {3}'.format(a, s, m, d))


# In[ ]:




