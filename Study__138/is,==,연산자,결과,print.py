#!/usr/bin/env python
# coding: utf-8

# is: 값이 같아도 주소값이 다르면 다르다(리스트에 적용)
# 
# == ; 값이 같으면, 같다

# In[5]:


a = 101
b = 100 + 1

print(a is b)#False
print(a == b)#True
print(id(a),id(b)) #is가 True인 이유


# In[6]:


c = 'korea'
d = 'korea'

print(c is d)# True
print(c == d)#True
print(id(c),id(d))


# In[7]:


e = [1,2,3,4,5]
f = [1,2,3,4,5]

print(e is f)#True
print(e == f)#True
print(id(e),id(f))


# In[10]:


z = "korea"
print('[1]',z,id(z))#k,korea
#k라고 한 이유는 인덱스로 생각했는데, ''를 보지 못함


# In[11]:


x = "korea"
print('[2]',x,id(x)) #[2] korea
print(z is x)#True


# In[12]:


z += "!"
print('[3]',z,id(z))#[3],korea!
print(x is z)# False


# In[13]:


y = z[:-1]
print('[4]', y, id(y))#[4], korea

print(z is y )#False


# In[ ]:




