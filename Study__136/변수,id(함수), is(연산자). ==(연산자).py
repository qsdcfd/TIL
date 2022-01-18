#!/usr/bin/env python
# coding: utf-8

# In[1]:


#id() 함수:주소값


a = '붕어빵'

print(a,' --> ',id(a) )

b = a

print(b, ' --> ',id(b) )

a = '잉어빵'

print(a,' --> ',id(a) )

#b=a는 복사가 되어기에 같은 것으로 나온다
#a가 할당 변수가 바뀌었기에 id()값이 다르게 나온다.


# ![image.png](attachment:image.png)
# 
# ![image-2.png](attachment:image-2.png)

# In[3]:


# is 연산자 
# 두 개가 맞고 틀린지를 True or False
# is연산자는 ==연산자와 달리 같은 객체를 가리키는지 비교

# 같은 값을 같더라도, 다르게 생성된 객체라면 is연산자로 False

##C의 값이 다른 이유는? 할당된 값은 같더라도 주소값이 다르다.

A = [1,2,3,4,5]

B = A

C = [1,2,3,4,5]

print(A is B)

print(A is C)

print(B is C)

print(id(A))

print(id(B))

print(id(C))



# In[4]:


# == 연산자

# == 연산자는 객체의 데이터 값이 같은지 확인할 때 사용

a = [1,2,3,4,5]

b = a

c = [1,2,3,4,5]

print(a == b)

print(a == c)

print(b == c)


# In[ ]:




