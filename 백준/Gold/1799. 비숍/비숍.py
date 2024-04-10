import sys
input = sys.stdin.readline

def dfs(idx, cnt):
    global ans
    # 가지치기 (남은자리 다 놓아도 정답갱신 안되는 경우)
    if cnt + (2*n-1 - idx) <= ans:
        return
    # 종료조건
    if idx == 2*n -1:
        if cnt > ans:
            ans = cnt
        return
    # 하부함수
    for x, y in lst[idx]: # 고르기
        if not v[x-y]:
            v[x-y] = 1
            dfs(idx + 1, cnt + 1)
            v[x-y] = 0
    dfs(idx + 1, cnt) # 안고르기

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
lst = [[] for _ in range(2*n-1)]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1:
            lst[i+j].append((i, j))
ans = 0
v = [0] * 30
dfs(0, 0)
print(ans)