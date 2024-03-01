# 1큰 방으로 이동
from collections import deque
def bfs(i, j):
    global mx, mnval
    q = deque([(i, j)])
    ans = [arr[i][j]]
    while q:
        x, y = q.popleft()
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if 0<=nx<n and 0<=ny<n and abs(arr[nx][ny]-arr[x][y])==1 and v[nx][ny] != 1:
                q.append((nx, ny))
                ans.append(arr[nx][ny])
                v[nx][ny] = 1
    # 큐에 아무것도 없으면
    if len(ans) > mx or ( len(ans) == mx and min(ans)<mnval ):
        mx, mnval = len(ans), min(ans)

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]
    mx = 0
    mnval = n*n+1
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                v[i][j] = 1
                bfs(i,j)
    print(f'#{tc} {mnval} {mx}')