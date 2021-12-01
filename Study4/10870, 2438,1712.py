#!/usr/bin/env python
# coding: utf-8

# In[5]:


def fibonacci(a):
    if a<=1:
        return a
    return fibonacci(a-1) + fibonacci(a-2)

n =int(input())
print(fibonacci(n))


# In[ ]:


n = int(input())

for i in range(1,n+1):
    print("*" * i)
    


# In[7]:


A,B,C = map(int,input().split())

if B>=C:
    print(-1)
else:
    print(int(A/(C-B))+1)


# In[ ]:




