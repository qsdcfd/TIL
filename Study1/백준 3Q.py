#!/usr/bin/env python
# coding: utf-8

# ![image](https://user-images.githubusercontent.com/86671456/132934283-9a7cbb75-f106-47e9-a5fa-2c781d9519ad.png)
# 

# In[ ]:


A,B =map(int,input().split())
if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


# ![image](https://user-images.githubusercontent.com/86671456/132934302-0b0e65da-2b1c-4647-ba98-4502f6f04cbc.png)
# 

# In[ ]:


N = int(input())
for i in range(1,10):
     print(N,'*', i,'=',  N*i)


# ![image](https://user-images.githubusercontent.com/86671456/132934525-b7cac08f-be00-4fc6-8172-e074fbeb5e0d.png)
# 

# In[ ]:


while True:

     A,B=map(int,input().split())
     if A == 0 and B ==0 :
        break;
     else:
        print(A +B)
        

