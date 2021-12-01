#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from math import gcd

def lcm(x,y):
    return x*y // gcd(x,y)
n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    print(lcm(a,b))


# In[ ]:


import sys
input = sys.stdin.readline

n, m, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
visited = [[False] * m for _ in range(n)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

answer = -1000000

def go(px, py, index, sum):
    if index == k:
        global answer
    
        if answer < sum:
            answer = sum
        
        return

    for x in range(px, n):
        for y in range(py if x==px else 0, m):
            
            if visited[x][y]:
                continue

            ok = True
            
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny]:
                        ok = False            
           
            if ok:
                visited[x][y] = True
                go(x, y, index+1, sum+arr[x][y])
                visited[x][y] = False


go(0, 0, 0, 0)

print(answer)


# In[ ]:


import sys
from itertools import combinations


n, l, r, x = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
result = 0
for i in range(2, n + 1):
    for comb in combinations(arr, i):
        if l <= sum(comb) <= r:
            if max(comb) - min(comb) >= x:
                result += 1

print(result)


# In[ ]:


import sys
input = sys.stdin.readline

def bf(start):
    dist[start] = 0
    for i in range(1, n+1):
        for s in range(1, n+1):
            for next, time in graph[s]:
                if dist[next] > dist[s] + time:
                    dist[next] = dist[s] + time
                    if i == n: #n번 이후에도 값이 갱신되면 음수 사이클 존재.
                        return True
    return False

TC = int(input())
for i in range(TC):
    n, m, w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [10001 for _ in range(n+1)]
    for j in range(m):
        s, e, t = map(int, input().split())
        graph[s].append([e, t])
        graph[e].append([s, t])
    for k in range(w):
        s, e, t = map(int, input().split())
        graph[s].append([e, -t])

    negative_cycle = bf(1)
    if not negative_cycle:
        print("NO")
    else:
        print("YES")

