#!/usr/bin/env python
# coding: utf-8

# In[6]:


H,M = map(int,input().split())

if M<45:
    if H ==0:
        H =23
        M +=60
    else:
        H -=1
        M +=60
print(H,M-45)


# In[9]:


N = int(input())
for i in range(1,N+1):
    print(i)


     


# In[19]:


A = int(input())
B = int(input())
C = int(input())
result =list(str(A * B *C)) # 숫자의 개수를 하려면 결과값이 문자열.

for i in range(10):
    print(result.count(str(i))) #고로 문자열로 갯수 계산


# In[17]:





# In[ ]:





# In[ ]:




