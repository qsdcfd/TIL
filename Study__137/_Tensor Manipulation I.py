#!/usr/bin/env python
# coding: utf-8

# ### Key-points
# 
# - 텐서(Tensor)
# 
# - 넘파이(NumPy)
# 
# - 텐서 조작(Tensor Manipulation)
# 
# - 브로드캐스팅(Broadcasting)
# 
# #### Learning
# 
# - Vector, Matrix and Tensor
# 
# - Numpy Review
# 
# - PyTorch Tensor Allocation
# 
# - Matrix Multiplication
# 
# - Other Basic Ops
# 

# ##### Vector, Matrix and Tensor
# 
# *Preview
# 
# ![image.png](attachment:image.png)
# 
# *2D Tensor(Typical Simple Setting)
# 
#    - |t| = (batch size, dim)
#    
# ![image-2.png](attachment:image-2.png)
# 
# 
# *3D Tensor(Typical Computer Vision)
# 
#    - |t| = (batch size, width, height)
#    
# ![image-3.png](attachment:image-3.png)
# 
# *3D Tensor(Typical NLP)
# 
#    - |t| = (batch size, length, dim)
#    
# ![image-4.png](attachment:image-4.png)
# 
# 

# ##### Numpy Review
# 
# Numpy와 Pytorch는 서로 호환이 너무 잘 되어서 직관적 이해가 편합니다.
# 

# In[5]:


#파이토치 설치
get_ipython().system(' pip install torchvision')


# In[6]:


import numpy as np
import torch


# In[7]:


#1D Array with Numpy

t = np.array([0., 1., 2., 3., 4., 5., 6.])
print(t)


# In[8]:


print('Rank of t :', t.ndim) #t의 차원
print('Shape of t:', t.shape)#행렬 형태


# In[9]:


print('t[0] t[1] t[-1] = ', t[0], t[1], t[-1])#Element
print('t[2:5] t[4:-1] = ', t[2:5], t[4:-1]) #Slicing
print('t[:2] t[3:] = ', t[:2], t[3:])#Slicing


# In[12]:


#1D Array with PyTorch

a = torch.FloatTensor([0.,1.,2.,3.,4.,5.,6.])
print(a)


# In[15]:


print(a.dim()) # rank, 차원
print(a.shape) #shape 행렬
print(a.size()) # shape
print(a[0], a[1], a[-1]) #Element
print(a[2:5], a[4:-1]) #Slicing
print(a[:2], a[3:])#Slicing


# In[10]:


#2D Array with Numpy

k = np.array([[1., 2., 3.], [4., 5., 6.],[7.,8.,9.], [10.,11.,12.]])
print(k)


# In[11]:


print('Rank of k: ', k.ndim)#k차원
print('Shape of k: ', k.shape)#행렬 형태


# In[16]:


#2D Array with PyTorch

b = torch.FloatTensor([[1., 2., 3.],
                       [4., 5., 6.],
                       [7., 8., 9.],
                       [10., 11., 12.]])
print(b)


# In[17]:


print(b.dim()) #rank
print(b.size()) #shape
print(b[:, 1])
print(b[:, 1].size())
print(b[:, :-1])


# ##### Broadcasting
# 
# 

# In[18]:


# Same shape

a =  torch.FloatTensor([[3,3]])
b = torch.FloatTensor([[2,2]])

print(a + b)


# In[19]:


#Vector + Scalar

a1 = torch.FloatTensor([[1, 2]])
a2 = torch.FloatTensor([3]) # 3 --> [[3,3]]

# 사이즈가 달라도 사이즈를 맞혀준다
print(a1 + a2)


# In[20]:


# 2 x 1 vector + 1 x 2 vector

b1 = torch.FloatTensor([[1, 2]])
b2 = torch.FloatTensor([[3], [4]])#[3,3], [4,4]
print(b1 + b2)


# ##### Multiplication vs Matrix Multiplication
# 
# 

# In[22]:


print()
print('-----------')
print('Mul vs Matmul')
print('-----------')

a = torch.FloatTensor([[1, 2], [3, 4]])
b = torch.FloatTensor([[1], [2]])

print('Shape of Matrix 1: ', a.shape) #2x2
print('Shape of Matrix 2: ', b.shape) #2x1
print(a.matmul(b)) #2x1

c = torch.FloatTensor([[1, 2], [3, 4]])
d = torch.FloatTensor([[1], [2]])

print('Shape of Matrix 1: ', c.shape) #2x2
print('Shape of Matrix 2: ', d.shape) #2x1
print(c.mul(d)) #2x1


# ##### Mean

# In[23]:


k = torch.FloatTensor([1,2])
print(k.mean())


# In[24]:


#Can't use mean() on integers

k1 = torch.LongTensor([1, 2])

try:
    print(k1.mean())
    
except Exception as exc:
    print(exc)


# In[25]:


k2 = torch.FloatTensor([[1, 2], [3, 4]])
print(k2)


# In[27]:


print(k2.mean())
print(k2.mean(dim=0))
print(k2.mean(dim=1))
print(k2.mean(dim=-1))


# ##### Max and Argmax
# 
# 

# In[29]:


r = torch.FloatTensor([[10, 20], [30, 40]])
print(r)


# In[30]:


print(r.max())# Returns on value: max


# In[31]:


print(r.max(dim = 0))
print('Max: ', r.max(dim=0)[0])
print('Argmax: ', r.max(dim=0)[1])


# In[32]:


print(r.max(dim=1))
print(r.max(dim=-1))


# In[ ]:




