#!/usr/bin/env python
# coding: utf-8

# 배열은 가까이에~ 기본 통계 데이터를 계산해 볼까?
# 1. 평균 계산하기
# 2. 배열을 활용한 평균, 표준편차, 중앙값 계산
# 
# 끝판왕 등장! numpy로 이 모든걸 한방에!
# 1. NumPy 소개
# 2. 주요기능
# 3. NumPy로 기본 통계 데이터 계산 해보기
# 
# 데이터의 행렬 변환
# 1. 이미지 데이터의 행렬 변환
# 
# 구조화된 데이터란?
# 1. 간단한 dictionary를 활용한 판타지 게임 logic 설계
# 2. 구조화된 데이터와 pandas
# 3. Pandas와 함께 EDA 시작하기
# 
# 

# 1)평균 구하기
# i) 숫자들의 합: total, 숫자의 개수:count로 변수명 지정
# ii) 초기값0
# iii) input함수 이용,숫자입력x->종료
# iv) while문(조건 지정반복문)
#    * 주의: input()의 return값은 str로 float로 변환필수
#    
#    조건:input() = ""
#        false
#        코딩 종료
#    조건: input()  = 숫자
#          True
#          count,total갱신
#          count +=1
#          total +=숫자
#          
# ex)코드 예시
# 
# total = 0
# count = 0
# numbers = input("Enter a number :  (<Enter Key> to quit)")
# while numbers != "":
#     try:
#         x = float(numbers)
#         count += 1
#         total = total + x
#     except ValueError:
#         print('NOT a number! Ignored..')
#     numbers = input("Enter a number :  (<Enter Key> to quit)")
# avg = total / count
# print("\n average is", avg)
#     
# 2)배열의 의미
# --> 요소들이 연속된 메모리 공간에 배치되고 동일 크기,타입 가진다.
#     
# ![image](https://user-images.githubusercontent.com/86671456/133353493-46aceafe-d06c-487e-927b-41c121576a19.png)
# https://hsm-edu.tistory.com/13
#     
# sample-입력 받은 숫자들
# count-입력 받은 샘플의 개수
# sample-평균값
#     -->입력받은 모든 숫자들 저장필요 by 리스트
#     
# 2-1)사용자가 입력한 숫자들을 배열로 만들기(동적배열)
#     # 2개 이상의 숫자를 입력받아 리스트에 저장하는 함수
# def numbers():
#     X=[]    # X에 빈 리스트를 할당합니다.
#     while True:
#         number = input("Enter a number (<Enter key> to quit)") 
#         while number !="":
#             try:
#                 x = float(number)
#                 X.append(x)    # float형으로 변환한 숫자 입력을 리스트에 추가합니다.
#             except ValueError:
#                 print('>>> NOT a number! Ignored..')
#             number = input("Enter a number (<Enter key> to quit)")
#         if len(X) > 1:  # 저장된 숫자가 2개 이상일 때만 리턴합니다.
#             return X
# 
# X=numbers()
# 
# print('X :', X)
# 
#     
# 2-2)list와 array의 차이
# 
# import array as arr
# 
# mylist = [1, 2, 3]   # 이것은 파이썬 built-in list입니다. 
# print(type(mylist))
# 
# mylist.append('4')  # mylist의 끝에 character '4'를 추가합니다. 
# print(mylist)
# 
# mylist.insert(1, 5)  # mylist의 두번째 자리에 5를 끼워넣습니다.
# print(mylist)
# 
# myarray = arr.array('i', [1, 2, 3])   # 이것은 array입니다. import array를 해야 쓸 수 있습니다.
# print(type(myarray))
# 
# # 아래 라인의 주석을 풀고 실행하면 에러가 납니다.
# #myarray.append('4')    # myarray의 끝에 character '4'를 추가합니다. 
# print(myarray)
# 
# myarray.insert(1, 5)    # myarray의 두번째 자리에 5를 끼워넣습니다.
# print(myarray)
#     
#     
# i)import필요X & built in 아님: array
# ii)처음부터 요소의 유형이 지정해서 생성하므로 추가불가
# iii)위의 반대가 list
#     
#     
# 3)리스트를 활용한 시그마의 표현
# range()-연속된 수를 리스트로 만들어줌
# len()-원소의 개수 구함
#     
# total = 0.0
# for i in range(len(X)):
#     total = total + X[i]
# mean = total / len(X)
# 
# print('sum of X: ', total)   
#     
# 4)중앙값
# --> 주어진 숫자를 크기 순서대로 배치할 때  가장 중앙.
#     i)n이 홀수이면 n/2을 반올림한 순서의 값
#     ii)n이 짝수라면 n/2번째 값과 ((n/2) + 1) 번째 값의        평균이 됩니다.
#     
#     
# def median(nums):  		# nums : 리스트를 지정하는 매개변수
#     nums.sort()					# sort()로 리스트를 순서대로 정렬
#     size = len(nums)
#     p = size // 2
#     if size % 2 == 0:		   # 리스트의 개수가 짝수                                   일때 
#         pr = p                         # 4번째 값
#         pl = p-1                      # 3번째 값
#         mid= float((nums[pl]+nums[pr])/2)    
#     else:								# 리스트의 개                                          수가 홀수일때
#         mid = nums[p]
#     return mid
# 
# print('X :', X)
# median(X)						# 매개변수의 값으로 X를 사용함
#     
# datalist=[1,7,5,6,5,7,8,1,23,7,8,6,2,4] 
# def median(data): 
#     d=len(data) 
#     data=sorted(data)
#     print('데이터 정렬 ',data) # 데이터가 짝수개 
#     if len(data)%2==0: 
#         d=int(d/2)
#         m=(data[d]+data[d-1])/2 return m # 데이터가 홀수개 
#     else: 
#         d=int(d/2)+1 
#         m=data[d] 
#         return m 
# print(len(datalist)) 
# median(datalist)
# 
# 출처: https://lsh-story.tistory.com/90 [빅데이터, 인공지능, 프로그래밍, 취미]    
#     
# 5) 표준편차와 평균
#     i)평균
#     
#     def means(nums):
#     total = 0.0
#     for i in range(len(nums)):
#         total = total + nums[i]
#     return total / len(nums)
# 
# means(X)
#     
#     ii)표준편차
# avg = means(X)
# 
# def std_dev(nums, avg):
#    texp = 0.0
#    for i in range(len(nums)):
#        texp = texp + (nums[i] - avg)**2    # 각 숫자와 평균값의 차이의 제곱을 계속 더한 후
#    return (texp/(len(nums)-1)) ** 0.5    # 그 총합을 숫자개수-1로 나눈 값의 제곱근을 리턴합니다.
# 
# std_dev(X,avg)
#     
# 6)전체 코드: main()함수
#     i)구현하고자 하는 값(평균값,중앙값,표준편차 by입력값)
#     ii)배열(리스트)로 만들기
#     iii)각 숫자의 평균값과 중앙값 구하기
#     iv)각 순자의 표준편파 구하기
#     
# med = median(X)
# avg = means(X)
# std = std_dev(X, avg)
# print("당신이 입력한 숫자{}의 ".format(X))
# print("중앙값은{}, 평균은{}, 표준편차는{}입니다.".format(med, avg, std))   

# In[ ]:


# 위의 전체 코드 정리

def numbers():
    X=[]
    while True:
        number = input("Enter a number (<Enter key> to quit)") 
        while number !="":
            try:
                x = float(number)
                X.append(x)
            except ValueError:
                print('>>> NOT a number! Ignored..')
            number = input("Enter a number (<Enter key> to quit)")
        if len(X) > 1:
            return X

def median(nums): 
    nums.sort()
    size = len(nums)
    p = size // 2
    if size % 2 == 0:
        pr = p
        pl = p-1
        mid = float((nums[pl]+nums[pr])/2)
    else:
        mid = nums[p]
    return mid

def means(nums):
    total = 0.0
    for i in range(len(nums)):
        total = total + nums[i]
    return total / len(nums)

def std_dev(nums, avg):
   texp = 0.0
   for i in range(len(nums)):
       texp = texp + (nums[i] - avg) ** 2
   return (texp/(len(nums)-1)) ** 0.5

def main():
    X = numbers()
    med = median(X)
    avg = means(X)
    std = std_dev(X, avg)
    print("당신이 입력한 숫자{}의 ".format(X))
    print("중앙값은{}, 평균은{}, 표준편차는{}입니다.".format(med, avg, std))

if __name__ == '__main__':
    main()


# Numpy
# 정의:데이터 분석에 필요한 파이썬 패키지
# https://blog.naver.com/reisei11/221762330326
# 장점: 
# i)신속 정확 그리고 다양한 연산 지원가능
# ii) 반복문 작성 필요 없다
# iii)배열 데이터를 디스크로 읽기 쓰기 가능(파일 저장o)
# iv)코드 통합
# 
# 1)ndarrary만들기
# 
# 문자열-->숫자(100%불가), 숫자-->문자열(100%가능)
# arange()
# array([])
# mport numpy as np  #  A와 B는 결과적으로 같은 ndarray 객체를 생성합니다. 
# A = np.arange(5)
# B = np.array([0,1,2,3,4])   #  A와 B는 결과적으로 같은 ndarray 객체를 생성합니다. 
# 
# C = np.array([0,1,2,3,'4']) # 파이썬 리스트를 numpy ndarray로 변환 # 하지만 C는 좀 다를 것입니다 
# D = np.ndarray((5,), np.int64, np.array([0,1,2,3,4])) # D도 A, B와 같은 결과를 내겠지만, B의 방법을 권합니다. 
# print(A)
# print(type(A))
# print(B)
# print(type(B))
# print(C)
# print(type(C))
# print(D)
# print(type(D))
# 
# 2)크기(size,shape,ndim)
#  * 원소 10개 = 행렬의 모양
#  
# 행렬 내  원소의 개수, 모양, 축의 개수 의미.
# reshape(): 행렬의 모양 바꾸기
# ndarray.size
# ndarray.shape
# ndarray.ndim
# reshape()
# 
# A = np.arange(10).reshape(2,5)   # 길이 10의 1차원 행렬을 2X5 2차원 행렬로 바꿔봅니다.
# 
# print(A.shape)
# print(A.ndim)
# print(A.size)
# 
# (2,5)
# 2
# 10
# 
# 3)type
# NumPy: numpy.array.dtype
# 파이썬: type()
# dtype:원소의 데이터타입 반환
# type():행렬의 자료형 반환
# 
# A= np.arange(6).reshape(2,3)
# print(A)
# print(A.dtype)
# print(type(A))
# 
# B = np.array([0,1,2,3,4,5])  
# print(B)
# print(B.dtype)
# print(type(B))
# 
# C = np.array([0,1,2,3,'4',5])
# print(C)
# print(C.dtype)
# print(type(C))
# 
# D = np.array([0,1,2,3,[4,5],6])  # 이런 ndarray도 만들어질까요?
# print(D)
# print(D.dtype)
# print(type(D))
# 
# [[0 1 2]
#  [3 4 5]]
# int64
# <class 'numpy.ndarray'>
# [0 1 2 3 4 5]
# int64
# <class 'numpy.ndarray'>
# ['0' '1' '2' '3' '4' '5']
# <U21
# <class 'numpy.ndarray'>
# [0 1 2 3 list([4, 5]) 6]
# object
# <class 'numpy.ndarray'>
# 
# 4)특수행렬
#   -단위행렬
# np.eye(3)
# 
# array([[1., 0., 0.],
#        [0., 1., 0.],
#        [0., 0., 1.]])
#   -0행렬
# np.zeros([2,3])
# 
# array([[0., 0., 0.],
#        [0., 0., 0.]])
#   -1행렬
# np.ones([3,3])
# 
# array([[1., 1., 1.],
#        [1., 1., 1.],
#        [1., 1., 1.]])
#        
# 5)브로드캐스트
# https://numpy.org/devdocs/user/basics.broadcasting.html
# :ndarray객체에 상수 연산을 하면 각각의 원소 연산적용
# A = np.arange(9).reshape(3,3)
# A
# 
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])
#        
#        # 3 X 3 행렬에 3 X 1 행렬을 더했을 때
# A = np.arange(9).reshape(3,3)
# C = np.array([[1], [2], [3]])
# print(A)
# print(C)
# A+C
# 
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[1]
#  [2]
#  [3]]
# array([[ 1,  2,  3],
#        [ 5,  6,  7],
#        [ 9, 10, 11]])
#        
# 6)슬라이드와 인덱싱
# Numpy에서 연산 가능
# 
# 7)random
# 난수 지원
# np.random.randint() :1개 정수형 난수
# np.random.choice() : 주어진 값 중 하나 고르기
# np.random.permutation() : 원소 순서 바꾸기
# np.random.normal() : 정규 분포 따름
# np.random.uniform() : 균등분포 따름
# 
# 8)전치 행렬
# :행렬의 행과 열을 맞바꾸기, 행렬의 축을 서로 바꾸기.
# arr.T
# np.transpose
# 
# A = np.arange(24).reshape(2,3,4)
# print(A)               # A는 (2,3,4)의 shape를 가진 행렬입니다. 
# print(A.T)            # 이것은 A의 전치행렬입니다. 
# print(A.T.shape) # A의 전치행렬은 (4,3,2)의 shape를 가진 행렬입니다.
# 
# [[[ 0  1  2  3]
#   [ 4  5  6  7]
#   [ 8  9 10 11]]
# 
#  [[12 13 14 15]
#   [16 17 18 19]
#   [20 21 22 23]]]
# [[[ 0 12]
#   [ 4 16]
#   [ 8 20]]
# 
#  [[ 1 13]
#   [ 5 17]
#   [ 9 21]]
# 
#  [[ 2 14]
#   [ 6 18]
#   [10 22]]
# 
#  [[ 3 15]
#   [ 7 19]
#   [11 23]]]
# (4, 3, 2)
# 
# 
# **** 기본 통계 데이터 계산 ******
# import numpy as np
# 
#   def numbers():
#     X = []
#     number = input("Enter a number (<Enter key> to quit)") 
#     # 하지만 2개 이상의 숫자를 받아야 한다는 제약조건을 제외하였습니다.
#     while number != "":
#         try:
#             x = float(number)
#             X.append(x)
#         except ValueError:
#             print('>>> NOT a number! Ignored..')
#         number = input("Enter a number (<Enter key> to quit)")
#     return X
# 
#   def main():
#     nums = numbers()       # 이것은 파이썬 리스트입니다. 
#     num = np.array(nums)   # 리스트를 Numpy ndarray로 변환합니다.
#     print("합", num.sum())
#     print("평균값",num.mean())
#     print("표준편차",num.std())
#     print("중앙값",np.median(num))   # num.median() 이 아님에 유의해 주세요.
# 
# main()

# <행렬의 데이터 변환>
# 1)소리, 이미지, 문자 표현법
# http://jalammar.github.io/visual-numpy/
# 
# 2)픽셀과 이미지
# 
# https://www.tensorflow.org/tutorials/images/data_augmentation
# 
# 이미지는 수많은 점(픽셀)들로 구성되어 있습니다.
# 각각의 픽셀은 R, G, B 값 3개 요소의 튜플로 색상이 표시됩니다. (Red, Green, Blue의 값이에요)
# 
# 2-1)라이브러리
# matplotlib
# PIL
# 
# import PIL
# PIL.__version__
# 
# 3)간단한 이미지 조작
# 
# open : Image.open() :메소드 이미지 파일 오픈
# size : Image.size : 가로* 세로 가각 튜플 값 반환 
# filename : Image.filename
# crop : Image.crop((x0, y0, xt, yt)) : 이미지 자르기(기로 세로의 시작점과 가로 세로의 종료점)
# resize : Image.resize((w,h))
# save : Image.save() :저장메소드
# 
# 4)행렬로 변환
# import numpy as np
# img_arr = np.array(img)
# print(type(img))
# print(type(img_arr))
# print(img_arr.shape)
# print(img_arr.ndim)

# In[1]:


import PIL
PIL.__version__


# In[2]:


# 파이썬 dict 로 표현한 전화번호부입니다. 
Country_PhoneNumber = {'Korea': 82, 'America': 1, 'Swiss': 41, 'Italy': 39, 'Japan': 81, 'China': 86, 'Rusia': 7}
Country_PhoneNumber['Korea']  # 키를 가지고 값을 조회할 수 있습니다.


# In[ ]:




