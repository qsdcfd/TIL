#!/usr/bin/env python
# coding: utf-8

# <클래스 상속 사용하기>
# --> 재사용 ㄱㄴ,효율성 good
# [클래스 상속 종류]
# 1) 기반 클래스(base class)
#  :기능을 물려주는 클래스
#  :부모 클래스(parent class), 슈퍼 클래스(superclass)라고 부르고, 파생 클래스는 자식 클래스(child class), 서브 클래스(subclass)라고도 부릅니다. 
# 2) 파생 클래스(derived class)
#  : 상속을 받아 새롭게 만드는 클래스
# 
# class 기반클래스이름:
#     코드
#  
# class 파생클래스이름(기반클래스이름):
#     코드 
#     
#     
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#  
# class Student(Person):
#     def study(self):
#         print('공부하기')
#  
# james = Student()
# james.greeting()    # 안녕하세요.: 기반 클래스 Person의 메서드 호출
# james.study()       # 공부하기: 파생 클래스 Student에 추가한 study 메서드
# https://dojang.io/pluginfile.php/13905/mod_page/content/2/036003.png
# 
# 3)상속 관계(명확하게 같은 종류, 동등관계)
# 
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#  
# class Student(Person):
#     def study(self):
#         print('공부하기')
#         
# 4)포함관계(상속 관계가 아닐 때 사용)
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#  
# class PersonList:
#     def __init__(self):
#         self.person_list = []    # 리스트 속성에 Person 인스턴스를 넣어서 관리
#  
#     def append_person(self, person):    # 리스트 속성에 Person 인스턴스를 추가하는 함수
#         self.person_list.append(person)
#         
# 5)기반 클래스 속성 사용
# : 기반 클래스에 있는 인스턴스 속성 사용
# - super().메서드() :.(점)을 붙여서 메서드 호출
# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'
#  
# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         super().__init__()                # super()로 기반 클래스의 __init__ 메서드 호출
#         self.school = '파이썬 코딩 도장'
#  
# james = Student()
# print(james.school)
# print(james.hello)
# https://dojang.io/pluginfile.php/13907/mod_page/content/3/036004.png
# 
# 6)기반 클래스를 초기화 하지 않아도 되는 경우
# 파생 클래스에서 _ init_ 메서드 생략하면 super() 사용안해도됨.
# class Person:
#     def __init__(self):
#         print('Person __init__')
#         self.hello = '안녕하세요.'
#  
# class Student(Person):
#     pass
#  
# james = Student()
# print(james.hello)
# 
# 7)메서드 오버라이딩 사용하기
# : 파생 클래스에서 기반 클래스의 메서드를 새로 정의.
# : 기반 클래스의 메서드를 무시하고 새로운 메서드 만든다
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#  
# class Student(Person):
#     def greeting(self):
#         print('안녕하세요. 저는 파이썬 코딩 도장 학생입니다.')
#  
# james = Student()
# james.greeting()
# 
# 8)다중 상속 사용하기
# : 여러 기반 클래스로부터 상속 받아서 파생 클래스 만든다
# : 클래스 (,) : 왼->오로 호출
# class 기반클래스이름1:
#     코드
#  
# class 기반클래스이름2:
#     코드
#  
# class 파생클래스이름(기반클래스이름1, 기반클래스이름2):
#     코드
#     
#     
# class Person:
#     def greeting(self):
#         print('안녕하세요.')
#  
# class University:
#     def manage_credit(self):
#         print('학점 관리')
#  
# class Undergraduate(Person, University):
#     def study(self):
#         print('공부하기')
#  
# james = Undergraduate()
# james.greeting()         # 안녕하세요.: 기반 클래스 Person의 메서드 호출
# james.manage_credit()    # 학점 관리: 기반 클래스 University의 메서드 호출
# james.study()            # 공부하기: 파생 클래스 Undergraduate에 추가한 study 메서드
# https://dojang.io/pluginfile.php/13909/mod_page/content/2/036005.png
# 
# 9)다이아몬드 상속
# https://dojang.io/pluginfile.php/13909/mod_page/content/2/068006.png
# 
# class A:
#     def greeting(self):
#         print('안녕하세요. A입니다.')
#  
# class B(A):
#     def greeting(self):
#         print('안녕하세요. B입니다.')
#  
# class C(A):
#     def greeting(self):
#         print('안녕하세요. C입니다.')
#  
# class D(B, C):
#     pass
#  
# x = D()
# x.greeting()    # 안녕하세요. B입니다
# 
# 
# 10)메서드 탐색 순서확인
# 클래스.mro()
# >>> D.mro()
# [<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]
# x = D()
# x.greeting()    # 안녕하세요. B입니다.

# 참고 | 상속 관계 확인하기
# 클래스의 상속 관계를 확인하고 싶을 때는 issubclass 함수를 사용합니다. 즉, 클래스가 기반 클래스의 파생 클래스인지 확인합니다. 기반 클래스의 파생 클래스가 맞으면 True, 아니면 False를 반환합니다.
# 
# issubclass(파생클래스, 기반클래스)
# 
# >>> class Person:
# ...     pass
# ...
# >>> class Student(Person):
# ...     pass
# ...
# >>> issubclass(Student, Person)
# True
# Student가 Person의 파생 클래스이므로 issubclass는 True가 나옵니다

# 참고 | 좀 더 명확하게 super 사용하기
# super는 다음과 같이 파생 클래스와 self를 넣어서 현재 클래스가 어떤 클래스인지 명확하게 표시하는 방법도 있습니다. 물론 super()와 기능은 같습니다.
# 
# super(파생클래스, self).메서드
# 
# class Student(Person):
#     def __init__(self):
#         print('Student __init__')
#         super(Student, self).__init__()     # super(파생클래스, self)로 기반 클래스의 메서드 호출
#         self.school = '파이썬 코딩 도장'

# 참고 | object 클래스
# 파이썬에서 object는 모든 클래스의 조상입니다. 그래서 int의 MRO를 출력해보면 int 자기 자신과 object가 출력됩니다.
# 
# >>> int.mro()
# [<class 'int'>, <class 'object'>]
# 파이썬 3에서 모든 클래스는 object 클래스를 상속받으므로 기본적으로 object를 생략합니다. 다음과 같이 클래스를 정의한다면
# 
# class X:
#     pass
# 괄호 안에 object를 넣은 것과 같습니다.
# 
# class X(object):
#     pass
# 파이썬 2에서는 class X:가 old-style 클래스를 만들고, class X(object):가 new-style 클래스를 만들었습니다. 그래서 파이썬 2에서는 이 둘을 구분해서 사용해야 했지만, 파이썬 3에서는 old-style 클래스가 삭제되었고 class X:와 class X(object): 모두 new-style 클래스를 만듭니다. 따라서 파이썬 3에서는 괄호 안에 object를 넣어도 되고 넣지 않아도 됩니다.
# 
# 11)추상 클래스
# : 메서드의 목록만 가진 클래스로 상속받는 클래스에서 메서드 구현 강제.
# from abc import *
#  
# class 추상클래스이름(metaclass=ABCMeta):
#     @abstractmethod
#     def 메서드이름(self):
#         코드
#         
#  rom abc import *
#  
# class StudentBase(metaclass=ABCMeta):
#     @abstractmethod
#     def study(self):
#         pass
#  
#     @abstractmethod
#     def go_to_school(self):
#         pass
#  
# class Student(StudentBase):
#     def study(self):
#         print('공부하기')
#  
#     def go_to_school(self):
#         print('학교가기')
#  
# james = Student()
# james.study()
# james.go_to_school()
# 
# 12.추상메서드를 빈 메서드로 만드는 이유
# : 추상 클래스는 인스턴스로 만들 수 없다.
# 그러므로 pass만 대입 왜냐하면 호출할 일이 없음
# :추상 클래스는 상속일 때만 사용.
#     @abstractmethod
#     def study(self):
#         pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦
#  
#     @abstractmethod
#     def go_to_school(self):
#         pass    # 추상 메서드는 호출할 일이 없으므로 빈 메서드로 만듦

# In[ ]:


class Bird(Animal,Wing):
    def fly(self):
        print('날다')

