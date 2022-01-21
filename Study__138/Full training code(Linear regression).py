#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install torchvision')


# In[2]:


import numpy as np
import torch


# In[3]:


#데이터 정의

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[2], [4], [6]])


# In[4]:


# Hypothesis초기화

W = torch.zeros(1, requires_grad = True)

b = torch.zeros(1, requires_grad = True)


# In[6]:


#Optimizer정의

optimizer = torch.optim.SGD([W, b], lr = 0.01)


# In[8]:


#Hypothesis 예측

nb_epochs = 1000
for epoch in range(1, nb_epochs + 1):
    hypothesis = x_train * W + b
    cost = torch.mean((hypothesis - y_train) ** 2)
    
    optimizer.zero_grad()
    cost.backward() #cost계산
    optimizer.step() #Optimizer로 학습


# In[ ]:




