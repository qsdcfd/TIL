#!/usr/bin/env python
# coding: utf-8

# < Unit 람다 표현식>
# :함수를 간편하게 작성이 가능하여 주로 인수 넣을 때 사용
# 
# 1) 람다표현식으로 함수 만들기
# 
# *람다표현식에선 이름 없는 함수를 만들기 때문에 호출 
# 하기 위해서 변수 할당해야 함
# 
# lambda 매개변수들: 식
# >>> plus_ten = lambda x: x + 10
# >>> plus_ten(1)
# 11
# 
# 2) 람다 표현식 자체를 호출하기
# (lambda 매개변수들: 식)(인수들)
# >>> (lambda x: x + 10)(1)
# 11
# 
# 3)람다 표현식 안에서는 변수를 만들 수 없다
# 그러므로 새 변수가 필요하면, def함수로 작성.
# >>> (lambda x: y = 10; x + y)(1)
# SyntaxError: invalid syntax
# 
# 허나, 람다 바깥에 있는 변수는 사용 가능
# >>> y = 10
# >>> (lambda x: x + y)(1)
# 11
# 
# 4)람다 표현식을 인수로 사용하기
# 
# 이유: 함수의 인수 부분에서 간단하게 함수 만들기
# EX)map()함수 이용
# >>> def plus_ten(x):
# ...     return x + 10
# ...
# >>> list(map(plus_ten, [1, 2, 3]))
# 
# 
# <람다 표현식>
# >>> list(map(lambda x: x + 10, [1, 2, 3]))
# 
# 5) 람다 표현식에 조건부 표현식 사용하기
# lambda 매개변수들: 식1 if 조건식 else 식2
# 
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(map(lambda x: str(x) if x % 3 == 0 else x, a))
# [1, 2, '3', 4, 5, '6', 7, 8, '9', 10]
# 
# lambda 매개변수들: 식1 if 조건식1 else 식2 if 조건식2 else 식3
# 
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
# 
# 
# 
# >>> def f(x):
# ...     if x == 1:
# ...         return str(x)
# ...     elif x == 2:
# ...         return float(x)
# ...     else:
# ...         return x + 10
# ...
# >>> a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# >>> list(map(f, a))
# ['1', 2.0, 13, 14, 15, 16, 17, 18, 19, 20]
# 
# 
# 6)map에 객체를 여러 개 넣기
# >>> a = [1, 2, 3, 4, 5]
# >>> b = [2, 4, 6, 8, 10]
# >>> list(map(lambda x, y: x * y, a, b))
# [2, 8, 18, 32, 50]
# 
# 7)filter사용하기
# filter(함수, 반복가능한객체)
# 
# 
# >>> def f(x):
# ...     return x > 5 and x < 10
# ...
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>> list(filter(f, a))
# [8, 7, 9]
# >>> def f(x):
# ...     return x > 5 and x < 10
# ...
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>> list(filter(f, a))
# [8, 7, 9]
# 
# 8)reduce사용하기
# 
# from functools import reduce
# reduce(함수, 반복가능한객체)
# 
# >>> def f(x, y):
# ...     return x + y
# ...
# >>> a = [1, 2, 3, 4, 5]
# >>> from functools import reduce
# >>> reduce(f, a)
# 15

# 참고 | 람다 표현식으로 매개변수가 없는 함수 만들기
# 람다 표현식으로 매개변수가 없는 함수를 만들 때는 lambda 뒤에 아무것도 지정하지 않고 :(콜론)을 붙입니다. 단, 콜론 뒤에는 반드시 반환할 값이 있어야 합니다. 왜냐하면 표현식(expression)은 반드시 값으로 평가되어야 하기 때문입니다.
# 
# >>> (lambda : 1)()
# 1
# >>> x = 10
# >>> (lambda : x)()
# 10

# 참고 | map, filter, reduce와 리스트 표현식
# 리스트(딕셔너리, 세트) 표현식으로 처리할 수 있는 경우에는 map, filter와 람다 표현식 대신 리스트 표현식을 사용하는 것이 좋습니다. list(filter(lambda x: x > 5 and x < 10, a))는 다음과 같이 리스트 표현식으로도 만들 수 있습니다.
# 
# >>> a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
# >>> [i for i in a if i > 5 and i < 10]
# [8, 7, 9]
# 리스트 표현식이 좀 더 알아보기 쉽고 속도도 더 빠릅니다.
# 
# 또한, for, while 반복문으로 처리할 수 있는 경우에도 reduce 대신 for, while을 사용하는 것이 좋습니다. 왜냐하면 reduce는 코드가 조금만 복잡해져도 의미하는 바를 한 눈에 알아보기가 힘들기 때문입니다. 이러한 이유로 파이썬 3부터는 reduce가 내장 함수에서 제외되었습니다.
# 
# reduce(lambda x, y: x + y, a)는 다음과 같이 for 반복문으로 표현할 수 있습니다.
# 
# >>> a = [1, 2, 3, 4, 5]
# >>> x = a[0]
# >>> for i in range(len(a) - 1):
# ...     x = x + a[i + 1]
# ...
# >>> x
# 15

# In[2]:


list(map(lambda x: x + 10, [1, 2, 3]))


# In[ ]:


list(map(lambda x:'{0:03d}'.format(int(x.split('.')[0]))+'.'+x.split('.')[1],files)) 


# In[6]:


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(lambda x: str(x) if x % 3 == 0 else x, a))
[1, 2, '3', 4, 5, '6', 7, 8, '9', 10]


def f(x):
    if x % 3 ==0:
        return str(x)
    else:
        return x
        
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list(map(f,a))


# In[ ]:




