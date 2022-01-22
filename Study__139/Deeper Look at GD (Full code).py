#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system(' pip install torchvision')


# In[2]:


get_ipython().system(' pip install --upgrade pip')


# In[4]:


import numpy as np
import torch


# In[6]:


#데이터

x_train = torch.FloatTensor([[1], [2], [3]])
y_train = torch.FloatTensor([[1], [2], [3]])

#모델 초기화

W = torch.zeros(1)

#lr설정

lr = 0.1

nb_epochs = 10 #데이터 학습 횟수

for epoch in range(nb_epochs + 1):
    
#학습하면서, 1에 수렴하는 W와 줄어드는 cost
    
    #H(x)계산
    
    hypothesis = x_train * W
    
    #cost gradient 계산
    
    cost = torch.mean((hypothesis - y_train) ** 2)
    gradient = torch.sum((W * x_train - y_train) * x_train)
    
    print('Epoch {:4d}/{} W: {:.3f}, Cost: {:.6f}'.format(
        epoch, nb_epochs, W.item(), cost.item()
    ))
    
    # cost gradient로 H(x)계산
    
    W -= lr * gradient


# In[8]:


#Full Code with torch.optim
#데이터

a_train = torch.FloatTensor([[1], [2], [3]])
b_train = torch.FloatTensor([[1], [2], [3]])

#모델 초기화

w = torch.zeros(1)

#lr설정

lr = 0.1

nb_epochs = 20 #데이터 학습 횟수

for epoch in range(nb_epochs + 1):
    
#학습하면서, 1에 수렴하는 W와 줄어드는 cost
    
    #H(x)계산
    
    hypothesis = a_train * w
    
    #cost gradient 계산
    
    cost = torch.mean((hypothesis - b_train) ** 2)
    gradient = torch.sum((w * a_train - b_train) * a_train)
    
    print('Epoch {:4d}/{} w: {:.3f}, Cost: {:.6f}'.format(
        epoch, nb_epochs, w.item(), cost.item()
    ))
    
    # cost gradient로 H(x)계산
    
    w -= lr * gradient


# In[ ]:




