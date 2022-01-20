#!/usr/bin/env python
# coding: utf-8

# ### 차례
# 
# - View 
# 
# - Squeeze 
# 
# - Unsqueeze 
# 
# - Type Casting
# 
# - Concatenate 
# 
# - Stacking
# 
# - In-place Operation

# In[2]:


get_ipython().system(' pip install torchvision')


# ##### View(Reshape)

# In[5]:


t = np.array([[[0, 1, 2],
               [3, 4, 5]],
             
              [[6, 7, 8],
               [9, 10, 11]]])

ft = torch.FloatTensor(t)
print(ft.shape)


# In[6]:


print(ft.view([-1,3]))
print(ft.view([-1,3]).shape)


# In[7]:


print(ft.view([-1, 1, 3]))
print(ft.view([-1, 1, 3]).shape)


# ##### Squeeze
# 

# In[9]:


import torch
import numpy as np


Ft = torch.FloatTensor([[0], [1], [2]])
print(Ft)
print(Ft.shape)


# In[10]:


print(Ft.squeeze())
print(Ft.squeeze().shape)


# ##### Unsqueeze
# 

# In[13]:


FT = torch.Tensor([0,1,2])
print(FT.shape)


# In[14]:


print(FT.unsqueeze(0))
print(FT.unsqueeze(0).shape)


# In[15]:


print(FT.view(1, -1))
print(FT.view(1, -1).shape)


# In[16]:


print(FT.unsqueeze(1))
print(FT.view(1, -1).shape)


# In[17]:


print(FT.unsqueeze(1))
print(FT.unsqueeze(1).shape)


# In[18]:


print(FT.unsqueeze(-1))
print(FT.unsqueeze(-1).shape)


# ##### Type Casting
# 
# 

# In[19]:


lt = torch.LongTensor([1,2,3,4])
print(lt)


# In[20]:


print(lt.float())


# In[21]:


bt = torch.ByteTensor([True, False, False, True])
print(bt)


# In[22]:


print(bt.long())
print(bt.float())


# ##### Concatenate

# In[23]:


x = torch.FloatTensor([[1,2], [3, 4]])
y = torch.FloatTensor([[5,6], [7,8]])


# In[24]:


print(torch.cat([x, y], dim = 0))
print(torch.cat([x, y], dim = 1))


# ##### Stacking

# In[25]:


x1 = torch.FloatTensor([1, 4])
y1 = torch.FloatTensor([2, 5])
z1 = torch.FloatTensor([3, 6])


# In[26]:


print(torch.stack([x1, y1, z1]))
print(torch.stack([x1, y1, z1], dim =1))


# In[28]:


print(torch.cat([x1.unsqueeze(0),y1.unsqueeze(0), z1.unsqueeze(0)], dim = 0))


# ##### Ones and Zeros
# 

# In[29]:


x = torch.FloatTensor([[0, 1, 2], [2, 1, 0]])
print(x)


# In[30]:


print(torch.ones_like(x))
print(torch.zeros_like(x))


# ##### In-place Operation
# 
# 

# In[31]:


x2 = torch.FloatTensor([[1, 2], [3, 4]])

print(x2.mul(2.))
print(x2)
print(x2.mul_(2.))
print(x2)


# In[ ]:




