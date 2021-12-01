#!/usr/bin/env python
# coding: utf-8

# 1. 클래스와 메서드 만들기
# 
# class 클래스이름:
#     def 메서드(self):
#         코드
#  
#  * 인스턴스 = 클래스()
#  
# 2.메서드 호출하기 
# * 인스턴스.메서드()
# 
# 3. 인스턴스와 객체의 차이점
# 인스턴스와 객체는 같은 것이지만, 보통 객체만 지정하면
# 객체. 근데 클래스와 연관이 되면 인스턴스
# 
# 4.속성 사용하기
# class 클래스이름:
#     def __init__(self):
#         self.속성 = 값
#         
# class Person:
#     def __init__(self): # 인스턴스를 만들때 호출되는 메서드(객체 초기화)
#         self.hello = '안녕하세요.'
#  
#     def greeting(self):
#         print(self.hello)
#  
# james = Person()
# james.greeting()    # 안녕하세요.
# 
# 5.self 의미
# self는 인스턴스 자기 자신을 의미.
# https://dojang.io/pluginfile.php/13877/mod_page/content/3/034004.png
# 
# 6.인스턴스를 만들 때 값 받기
# class 클래스이름:
#     def __init__(self, 매개변수1, 매개변수2):
#         self.속성1 = 매개변수1
#         self.속성2 = 매개변수2
#  
#  
#  class Person:
#     def __init__(self, name, age, address):
#         self.hello = '안녕하세요.'
#         self.name = name
#         self.age = age
#         self.address = address
#  
#     def greeting(self):
#         print('{0} 저는 {1}입니다.'.format(self.hello, self.name))
#  
# maria = Person('마리아', 20, '서울시 서초구 반포동')
# maria.greeting()    # 안녕하세요. 저는 마리아입니다.
#  
# print('이름:', maria.name)       # 마리아
# print('나이:', maria.age)        # 20
# print('주소:', maria.address)    # 서울시 서초구 반포동
# 
# 7.비공개 속성 사용하기
# :클래스 안에서만 사용하고 바깥에선 접근 금지.

# 참고 | 빈 클래스 만들기
# 내용이 없는 빈 클래스를 만들 때는 코드 부분에 pass를 넣어줍니다.
# 
# class Person:
#     pass
# 참고 | 메서드 안에서 메서드 호출하기
# 메서드 안에서 메서드를 호출할 때는 다음과 같이 self.메서드() 형식으로 호출해야 합니다. self 없이 메서드 이름만 사용하면 클래스 바깥쪽에 있는 함수를 호출한다는 뜻이 되므로 주의해야 합니다
# 
# class Person:
#     def greeting(self):
#         print('Hello')
#  
#     def hello(self):
#         self.greeting()    # self.메서드() 형식으로 클래스 안의 메서드를 호출
#  
# james = Person()
# james.hello()    # Hello
# 참고 | 특정 클래스의 인스턴스인지 확인하기
# 현재 인스턴스가 특정 클래스의 인스턴스인지 확인할 때는 isinstance 함수를 사용합니다. 특정 클래스의 인스턴스가 맞으면 True, 아니면 False를 반환합니다.
# 
# isinstance(인스턴스, 클래스)
# 
# >>> class Person:
# ...     pass
# ...
# >>> james = Person()
# >>> isinstance(james, Person)
# True
# isinstance는 주로 객체의 자료형을 판단할 때 사용합니다. 예를 들어 팩토리얼 함수는 1부터 n까지 양의 정수를 차례대로 곱해야 하는데, 실수와 음의 정수는 계산할 수 없습니다. 이런 경우에 isinstance를 사용하여 숫자(객체)가 정수일 때만 계산하도록 만들 수 있습니다.
# 
# def factorial(n):
#     if not isinstance(n, int) or n < 0:    # n이 정수가 아니거나 음수이면 함수를 끝냄
#         return None
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)

# 참고 | 클래스의 위치 인수, 키워드 인수
# 클래스로 인스턴스를 만들 때 위치 인수와 키워드 인수를 사용할 수 있습니다. 규칙은 함수와 같습니다. 위치 인수와 리스트 언패킹을 사용하려면 다음과 같이 *args를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 args[0]처럼 사용해야 합니다.
# 
# class Person:
#     def __init__(self, *args):
#         self.name = args[0]
#         self.age = args[1]
#         self.address = args[2]
#  
# maria = Person(*['마리아', 20, '서울시 서초구 반포동'])
# 키워드 인수와 딕셔너리 언패킹을 사용하려면 다음과 같이 **kwargs를 사용하면 됩니다. 이때 매개변수에서 값을 가져오려면 kwargs['name']처럼 사용해야 합니다.
# 
# class Person:
#     def __init__(self, **kwargs):    # 키워드 인수
#         self.name = kwargs['name']
#         self.age = kwargs['age']
#         self.address = kwargs['address']
#  
# maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
# maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})

# 참고 | 인스턴스를 생성한 뒤에 속성 추가하기, 특정 속성만 허용하기
# 지금까지 클래스의 인스턴스 속성은 __init__ 메서드에서 추가한 뒤 사용했습니다. 하지만 클래스로 인스턴스를 만든 뒤에도 인스턴스.속성 = 값 형식으로 속성을 계속 추가할 수 있습니다. 다음 Person 클래스는 빈 클래스이지만 인스턴스를 만든 뒤 name 속성을 추가합니다.
# 
# >>> class Person:
# ...     pass
# ...
# >>> maria = Person()         # 인스턴스 생성
# >>> maria.name = '마리아'    # 인스턴스를 만든 뒤 속성 추가
# >>> maria.name
# '마리아'
# 이렇게 추가한 속성은 해당 인스턴스에만 생성됩니다. 따라서 클래스로 다른 인스턴스를 만들었을 때는 추가한 속성이 생성되지 않습니다.
# 
# >>> james = Person()    # james 인스턴스 생성
# >>> james.name    # maria 인스턴스에만 name 속성을 추가했으므로 james 인스턴스에는 name 속성이 없음
# Traceback (most recent call last):
#   File "<pyshell#11>", line 1, in <module>
#     james.name
# AttributeError: 'Person' object has no attribute 'name'
# 인스턴스는 생성한 뒤에 속성을 추가할 수 있으므로 __init__ 메서드가 아닌 다른 메서드에서도 속성을 추가할 수 있습니다. 단, 이때는 메서드를 호출해야 속성이 생성됩니다.
# 
# >>> class Person:
# ...     def greeting(self):
# ...         self.hello = '안녕하세요'    # greeting 메서드에서 hello 속성 추가
# ...
# >>> maria = Person()
# >>> maria.hello    # 아직 hello 속성이 없음
# Traceback (most recent call last):
#   File "<pyshell#22>", line 1, in <module>
#     maria.hello
# AttributeError: 'Person' object has no attribute 'hello'
# >>> maria.greeting()    # greeting 메서드를 호출해야
# >>> maria.hello         # hello 속성이 생성됨
# '안녕하세요'
# 인스턴스는 자유롭게 속성을 추가할 수 있지만 특정 속성만 허용하고 다른 속성은 제한하고 싶을 수도 있습니다. 이때는 클래스에서 __slots__에 허용할 속성 이름을 리스트로 넣어주면 됩니다. 특히 속성 이름은 반드시 문자열로 지정해줍니다.
# 
# __slots__ = ['속성이름1, '속성이름2']
# 
# >>> class Person:
# ...     __slots__ = ['name', 'age']    # name, age만 허용(다른 속성은 생성 제한)
# ...
# >>> maria = Person()
# >>> maria.name = '마리아'                     # 허용된 속성
# >>> maria.age = 20                            # 허용된 속성
# >>> maria.address = '서울시 서초구 반포동'    # 허용되지 않은 속성은 추가할 때 에러가 발생함
# Traceback (most recent call last):
#   File "<pyshell#32>", line 1, in <module>
#     maria.address = '서울시 서초구 반포동'
# AttributeError: 'Person' object has no attribute 'address'

# 참고 | 공개 속성과 비공개 속성
# 클래스 바깥에서 접근할 수 있는 속성을 공개 속성(public attribute)이라 부르고, 클래스 안에서만 접근할 수 있는 속성을 비공개 속성(private attribute)이라 부릅니다.
# 
# 참고 | 비공개 메서드 사용하기
# 속성뿐만 아니라 메서드도 이름이 __(밑줄 두 개)로 시작하면 클래스 안에서만 호출할 수 있는 비공개 메서드가 됩니다.
# 
# class Person:
#     def __greeting(self):
#         print('Hello')
#  
#     def hello(self):
#         self.__greeting()    # 클래스 안에서는 비공개 메서드를 호출할 수 있음
#  
# james = Person()
# james.__greeting()    # 에러: 클래스 바깥에서는 비공개 메서드를 호출할 수 없음
# 비공개 메서드도 메서드를 클래스 바깥으로 드러내고 싶지 않을 때 사용합니다. 보통 내부에서만 호출되어야 하는 메서드를 비공개 메서드로 만듭니다. 예를 들어 게임 캐릭터가 마나를 소비해서 스킬을 쓴다고 치면 마나 소비량을 계산해서 차감하는 메서드는 비공개 메서드로 만들고, 스킬을 쓰는 메서드는 공개 메서드로 만듭니다. 만약 마나를 차감하는 메서드가 공개되어 있다면 마음대로 마나를 차감시킬 수 있으므로 잘못된 클래스 설계가 됩니다.

# In[ ]:


class Annie:
    def __init__(self,health,mana,ability_power):
        self.health=health
        self.mana=mana
        self.ability_power=ability_power
 
    def tibbers(self):
        print('티버: 피해량 {0}'.format(self.ability_power*0.65+400))

