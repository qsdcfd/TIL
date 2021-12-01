#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())

if n >= 90 and n <= 100:
    print('A')
elif n >=80 and n < 90:
    print('B')
elif n >=70 and n < 80:
    print('C')
elif n >=60 and n < 70:
    print('D')
else:
    print('F')


# In[ ]:


n = int(input())
for i in range(n):
    A,B=map(int,input().split())
    print(A+B)


# In[ ]:



while True:
    try:
        A,B=map(int,input().split())
        0<A and B<10

        print(A+B)
    except:
        break
    


# In[ ]:




