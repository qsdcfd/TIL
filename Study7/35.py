#!/usr/bin/env python
# coding: utf-8

# Unit35 클래스 속성과 정적, 클래스 메서드 사용하기
# 
# 1.클래스 속성과 인스턴스 속성 알아보기
#  i)클래스 속성
#  클래스 속성은 클래스에 속해 있으며 모든 인스턴스에서 공유
#  모든 인스턴스가 공유하므로 전체가 사용하는 값을 사용할 때 저장
#  클래스.속성
#  
#   class 클래스이름:
#     속성 = 값
# 
# 
# class Person:
#     bag = []
#  
#     def put_bag(self, stuff):
#         self.bag.append(stuff)
#  
# james = Person()
# james.put_bag('책')
#  
# maria = Person()
# maria.put_bag('열쇠')
#  
# print(james.bag)
# print(maria.bag)
# 
# https://dojang.io/pluginfile.php/13898/mod_page/content/6/035001.png
# 
# https://dojang.io/pluginfile.php/13898/mod_page/content/6/035002.png
# 
#  i+)
#  비공개 클래스속성
# class Knight:
#     __item_limit = 10    # 비공개 클래스 속성
#  
#     def print_item_limit(self):
#         print(Knight.__item_limit)    # 클래스 안에서만 접근할 수 있음
#  
#  
# x = Knight()
# x.print_item_limit()    # 10
#  
# print(Knight.__item_limit)    # 클래스 바깥에서는 접근할 수 없음
#  
#  
#  ii)인스턴스 속성 사용하기
#    :공유X
#    :독립성이 있어, 값을 따로 저장
#    class Person:
#     def __init__(self):
#         self.bag = []
#  
#     def put_bag(self, stuff):
#         self.bag.append(stuff)
#  
# james = Person()
# james.put_bag('책')
#  
# maria = Person()
# maria.put_bag('열쇠')
#  
# print(james.bag)
# print(maria.bag)
# 
# 
# 2)정적 메서드 사용하기
# 인스턴스 없이 호출
# 클래스.메서드()
# 
# class 클래스이름:
#     @staticmethod
#     def 메서드(매개변수1, 매개변수2):
#         코드
#         
# class Calc:
#     @staticmethod
#     def add(a, b):
#         print(a + b)
#  
#     @staticmethod
#     def mul(a, b):
#         print(a * b)
#  
# Calc.add(10, 20)    # 클래스에서 바로 메서드 호출
# Calc.mul(10, 20)    # 클래스에서 바로 메서드 호출        
# 
# 3)클래스 메서드
# 인스턴스 없이 호출.
# 메서드 안에서 클래스 속성, 클래스 메서드 접근
# cls사용--> 메서드 안에서 현재 클래스의 인스턴스 만들 수 있다
# 고로, cls는 클래스 이므로 cls() =prerson()
# class 클래스이름:
#     @classmethod
#     def 메서드(cls, 매개변수1, 매개변수2):
#         코드
#         
#         
# class Person:
#     count = 0    # 클래스 속성
#  
#     def __init__(self):
#         Person.count += 1    # 인스턴스가 만들어질 때
#                              # 클래스 속성 count에 1을 더함
#  
#     @classmethod
#     def print_count(cls):
#         print('{0}명 생성되었습니다.'.format(cls.count))    # cls로 클래스 속성에 접근
#  
# james = Person()
# maria = Person()
#  
# Person.print_count()    # 2명 생성되었습니다.

# 참고 | 속성, 메서드 이름을 찾는 순서
# 파이썬에서는 속성, 메서드 이름을 찾을 때 인스턴스, 클래스 순으로 찾습니다. 그래서 인스턴스 속성이 없으면 클래스 속성을 찾게 되므로 james.bag, maria.bag도 문제 없이 동작합니다. 겉보기에는 인스턴스 속성을 사용하는 것 같지만 실제로는 클래스 속성입니다.
# 
# 인스턴스와 클래스에서 __dict__ 속성을 출력해보면 현재 인스턴스와 클래스의 속성을 딕셔너리로 확인할 수 있습니다.
# 
# 인스턴스.__dict__
# 
# 클래스.__dict__
# 
# >>> james.__dict__
# {}
# >>> Person.__dict__
# mappingproxy({'__module__': '__main__', 'bag': ['책', '열쇠'], 'put_bag': <function Person.put_bag at 0x028A32B8>, '__dict__': <attribute '__dict__' of 'Person' objects>, '__weakref__': <attribute '__weakref__' of 'Person' objects>, '__doc__': None})
# </코드>
# 
# james.bag을 사용했을 때 클래스 속성을 찾는 과정은 다음과 같습니다.
# 
# 
# 

# 참고 | 클래스와 메서드의 독스트링 사용하기
# 함수와 마찬가지로 클래스와 메서드도 독스트링을 사용할 수 있습니다. 다음과 같이 클래스와 메서드를 만들 때 :(콜론) 바로 다음 줄에 """ """(큰따옴표 세 개) 또는 ''' '''(작은따옴표 세 개)로 문자열을 입력하면 됩니다. 그리고 클래스의 독스트링은 클래스.__doc__ 형식으로 사용하고, 메서드의 독스트링은 클래스.메서드.__doc__ 또는 인스턴스.메서드.__doc__ 형식으로 사용합니다.
# 
# class Person:
#     '''사람 클래스입니다.'''
#     
#     def greeting(self):
#         '''인사 메서드입니다.'''
#         print('Hello')
#  
# print(Person.__doc__)             # 사람 클래스입니다.
# print(Person.greeting.__doc__)    # 인사 메서드입니다.
#  
# maria = Person()
# print(maria.greeting.__doc__)     # 인사 메서드입니다.

# 참고 | 파이썬 자료형의 인스턴스 메서드와 정적 메서드
# 파이썬의 자료형도 인스턴스 메서드와 정적, 클래스 메서드로 나뉘어져 있습니다. 예를 들어 세트에 요소를 더할 때는 인스턴스 메서드를 사용하고, 합집합을 구할 때는 정적 메서드를 사용하도록 만들어져 있습니다.
# 
# >>> a = {1, 2, 3, 4}
# >>> a.update({5})    # 인스턴스 메서드
# >>> a
# {1, 2, 3, 4, 5}
# >>> set.union({1, 2, 3, 4}, {5})    # 정적(클래스) 메서드
# {1, 2, 3, 4, 5}
# 이처럼 인스턴스의 내용을 변경해야 할 때는 update와 같이 인스턴스 메서드로 작성하면 되고, 인스턴스 내용과는 상관없이 결과만 구하면 될 때는 set.union과 같이 정적 메서드로 작성하면 됩니다.

# In[ ]:


@staticmethod
   def is_time_valid(time_string):
     hour, minute, second = map(int, time_string.split(':'))
     return hour <= 24 and minute <= 59 and second <= 60

   @classmethod
   def from_string(cls, time_string):
     hour, minute, second = map(int, time_string.split(':'))
     return cls(hour, minute, second)

