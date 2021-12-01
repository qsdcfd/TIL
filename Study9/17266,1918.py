#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a = int(input())
b = int(input())

positions = list(map(int, input().split()))
len_positions = len(positions)

min_height = 0


if len_positions == 1:
    min_height = max(positions[0] - 0, a - positions[0])

else:
    for i in range(len_positions):
       
        if i == 0:
            height = positions[i] - 0
      
        elif i == len_positions - 1:
            height = a - positions[i]
        
        else:
            tmp = positions[i] - positions[i-1]
            if tmp % 2:
                height = tmp // 2 + 1
            else:
                height = tmp // 2
        
        min_height = max(height, min_height)

print(min_height)


# In[ ]:


strn = list(input())
stack=[]
res=''
for s in strn:
    if s.isalpha():
        res+=s
    else:
        if s == '(':
            stack.append(s)
        elif s == '*' or s == '/':
            while stack and (stack[-1] == '*' or stack[-1] =='/'):
                res += stack.pop()
            stack.append(s)
        elif s == '+' or s == '-':
            while stack and stack[-1] != '(':
                res+= stack.pop()
            stack.append(s)
        elif s == ')':
            while stack and stack[-1] != '(':
                res += stack.pop()
            stack.pop()
while stack :
    res+=stack.pop()
print(res)


출처: https://pannchat.tistory.com/entry/파이썬-백준-후위표기식-python [박지원]

