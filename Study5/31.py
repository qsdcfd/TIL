#!/usr/bin/env python
# coding: utf-8

# <재귀함수호출>
# 
# 1)재귀호출 사용하기
# def hello():
#     print('Hello, world!')
#     hello()
#  
# hello()
# 
# 
# https://dojang.io/pluginfile.php/13846/mod_page/content/3/031001.png
# 
# ->계속 진행되다가 초과하면 에러!
# 
# 2) 재귀호출에 종료 조건 만들기
# 
# def hello(count):
#     if count == 0:    # 종료 조건을 만듦. count가 0이면 다시 hello 함수를 호출하지 않고 끝냄
#         return
#     
#     print('Hello, world!', count)
#     
#     count -= 1      # count를 1 감소시킨 뒤
#     hello(count)    # 다시 hello에 넣음
#  
# hello(5)    # hello 함수 호출
# 
# https://dojang.io/pluginfile.php/13846/mod_page/content/3/031002.png
# 
# 3)재귀 호출로 팩토리얼 구하기
#   
#   * 반환값 부분이 핵심이다!
#   왜냐하면 바로 나오는 것이 아니라 재귀호출로 곱하는 과정을 반복하다가
#   n=1이 될 때 반환하기 때문이다.
# def factorial(n):
#     if n == 1:      # n이 1일 때
#         return 1    # 1을 반환하고 재귀호출을 끝냄
#     return n * factorial(n - 1)    # n과 factorial 함수에 n - 1을 넣어서 반환된 값을 곱함
#  
# print(factorial(5))
# 
# https://dojang.io/pluginfile.php/13847/mod_page/content/2/031003.png
# 
# https://dojang.io/pluginfile.php/13847/mod_page/content/2/031004.png
# 
# https://dojang.io/pluginfile.php/13847/mod_page/content/2/031005.png
# 
