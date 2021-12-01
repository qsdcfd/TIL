#!/usr/bin/env python
# coding: utf-8

# 함수(function): 불려진 시점에 특정한 작업을 수행하며, 입력값과 출력값(반환값)을 가질 수 있습니다.
# 인자(argument): 함수를 호출할 때 전달하는 입력값입니다.
# 매개변수(parameter): 함수가 실행될 때 입력값이 들어올 변수입니다.
# 반환값(return value): 함수가 종료될 때 호출지점으로 전달할 출력값입니다.
# 변수(variable): 값을 가리키는 이름입니다.
# 스코프(scope): 변수가 유효한 범위입니다.
# 연산자(operator): 주어진 값들에 대해 정해진 연산을 수행합니다.
# 수리 연산자(mathematical operator): +, -, *, /, //, **
# 비교 연산자(comparison operator): ==, !=, <, >, <=, >=, is
# 논리 연산자(logical operator): and, or
# 소속 연산자(membership operator): in
# 제어문(control statements): 코드 블럭의 흐름(실행 여부, 반복)을 제어합니다.
# if: 명제가 참이면 실행합니다.
# else: if 명제 이외의 경우에 실행합니다.
# elif: if 명제 이외의 경우에 또 다른 명제가 참일 경우에 실행합니다.
# while: 명제가 참일 동안 반복합니다.
# for: 주어진 값들 하나씩 반복합니다.
# 자료형(data types): 값들의 종류를 나타냅니다.
# 정수(int), 부동소수점 수(float), 불리언(bool), 문자열(str), 튜플(tuple), 리스트(list), 딕셔너리(dict)
# 
# 
# 
# prit()-문자열 출력
# 변수 정의: [변수명]=[변수값]
# def 함수명(): -->함수를 정의할 때 사용하는 일종의 예약어
# parameter: 입력값으로 주어진 인자를 받는 변수
# 스코프(scope): 정의된 변수가 어디까지 유효한지 정의된 범위
# global scope: 어디에서든 참조가능
# local scope: 내부에서 정의되어 밖에서 볼 수 없음
# if 명제:
# 명제가 참일 때만 실행.
# else:
# 명제가 거짓일 때만 실행
# conditional operator: >,<,>=,<=,==,!=
# fibonacci()함수[재귀함수]
# 
# def fibonacci(n):
#     if n <= 2:
#         return 1
#     else:
#         return fibonacci(n-2) + fibonacci(n-1)
# 
# n = 1
# while n <= 20:
#     print(fibonacci(n))
#     n = n + 1
# print('끝!')
# 
# loop: 반복문
# type(): 자료형
# NoneType
# bool: True or False를 반환하는 함수
# for문
# for 변수 in range:
#     print(변수)
# 
# 슬라이스
# 변수 = 변수값
# print(변수[:])--> 
# :를 써서 [n:m]처럼 n번째부터 m번 직전까지를 한 번에 뽑아올 수도 있습니다.
# 변수.append():값을 하나씩 추가
# 변수.remove():특정 값 빼기
# 변수.pop(): 특정 순서의 값 빼기
# 변수.items():키와 값을 둘 다 뽑을 수 있다.
# 
# if문에 딸린 조건문과 코드 블럭이 변경되었습니다. if n in memory를 통해 입력값 n이라는 키가 memory 딕셔너리에 이미 있는 경우, 그 값 memory[n]을 바로 number로써 반환하라는 이야기입니다.
# 이것은 메모이제이션(memoization)이고 이를 통해 계산시간을 줄입니다.
