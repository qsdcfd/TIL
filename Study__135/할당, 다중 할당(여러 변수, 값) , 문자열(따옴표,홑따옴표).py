#!/usr/bin/env python
# coding: utf-8

# In[13]:


#할당

a = b = c = d = 100, 200

print(a, type(a))

print(a,b,c,d)


# In[1]:


#다중할당

a,b,c,d= 100, 3.14, 'k', 'korea' 

#따옴표를 하지 않으면 syntax가 맞지 않게 되어 에러가 뜬다.
#즉, 숫자와 문자는 같이 할당되기 안됨

print(a,b,c,d)


# In[3]:



#의문

e = 100, 3.14, 'k', 'korea' 

#첫번 째만 받는 것이 아니라 다 받는다. 
#tuple형식

print(e, type(e))


# In[10]:


#문자열 
#쌍따옴표, 홑따옴표 출력
#""" """: 매직, 안에 있는 따옴표들 다 출력
#" ' '": '' 출력
#' " "': "" 출력

sample_txt1 = '나는 엄마에게 말했다. "더 이상 카레는 먹기 싫어요!"라고..'

sample_txt2 = """나는 엄마에게 말했다. "더 이상 '카레'는 먹기 싫어요!"라고.."""

#sample_txt2 = '나는 엄마에게 말했다."더 이상'카레'는 먹기 싫어요!"라고..'


print(sample_txt1)
print(sample_txt2)


# In[ ]:




