#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a=int(input())
b= list(map(int,input().split()))

print('{} {}'.format(min(a),max(b)))


# In[ ]:


a= []
for k in range(9):
    a.append(int(input()))
print(max(a), a.index(max(a)) +1)


# In[ ]:


N = int(input())
def fal(N):
    if N <= 1:
        return 1
    return N * fal(N-1)

print(fal(N))


# In[ ]:




