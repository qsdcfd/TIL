#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n = int(input())
a = list(map(int, input().split()))
sum = [a[0]]
for i in range(len(a) - 1):
    sum.append(max(sum[i] + a[i + 1], a[i + 1]))
print(max(sum))


# In[ ]:


from collections import deque

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
select = [False] * 10
q, v, k = deque(), [], 0

def bfs(dist):
    global ans
    infect, times = 0, 0
    while q:
        x, y = q.popleft()
        times = dist[x][y]
        for dx, dy in (-1,0), (1,0), (0,1), (0,-1):
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue
            if a[nx][ny] != 1 and dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx, ny))
                infect += 1
    if infect == k:
        ans = min(ans, times)

def solve(idx, cnt, d):
    if cnt == m:
        dist = [[-1]*n for _ in range(n)]
        for i in range(d):
            if select[i]:
                x, y = v[i]
                q.append((x, y))
                dist[x][y] = 0
        bfs(dist)
        return
    for i in range(idx, d):
        if not select[i]:
            select[i] = True
            solve(i+1, cnt+1, d)
            select[i] = False

for i in range(n):
    for j in range(n):
        if a[i][j] == 2:
            v.append((i, j))
        if a[i][j] == 0:
            k += 1
ans = 10**9
k = k+len(v)-m
solve(0, 0, len(v))
print(ans if ans != 10**9 else -1)


출처: https://rebas.kr/845 [PROJECT REBAS]

