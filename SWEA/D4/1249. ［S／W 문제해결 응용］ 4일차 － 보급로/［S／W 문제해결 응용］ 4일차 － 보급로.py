from collections import deque
 
def bfs(ei, ej):
    q = deque([(0, 0)])
    v = [['n'] * n for _ in range(n)]  # 'n' == 미방문
    v[0][0] = 0
 
    while q:
        i, j = q.popleft()
 
        for di, dj in ((1,0),(-1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if 0<= ni <n and 0<= nj <n: # 범위 내
                if v[ni][nj] == 'n' or v[i][j] + arr[ni][nj] < v[ni][nj]:  # 미방문 or 갱신예정값이 더 작을 때 -> 갱신
                    v[ni][nj] = v[i][j] + arr[ni][nj]
                    q.append((ni, nj))
                     
    return v[ei][ej]
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
 
    # 출발지 (0,0), 도착지(n-1, n-1)
    print(f'#{tc} {bfs(n-1, n-1)}')