# 시작칸 끝칸까지 세기
# 벽 k개 이하 부수기 가능
from collections import deque
INF = float('inf')

def bfs():
    q = deque([(0, 0, 0)])
    v = [[[INF] * m for _ in range(n)] for _ in range(k+1)]
    v[0][0][0] = 1

    while q:
        h, x, y = q.popleft()
        # q에 넣기
        for dx, dy in ((-1,0), (1,0), (0,1), (0,-1)):
            nx, ny = x + dx, y + dy
            if nx == n-1 and ny == m-1: # 도착점이고
                if v[h][nx][ny] > v[h][x][y] + 1: # 지금 이동거리가 더 작으면
                    v[h][nx][ny] = v[h][x][y] + 1 # 갱신
                    continue

            if 0<= nx < n and 0<= ny < m: # 상하좌우 범위 내
                if arr[nx][ny] == 1 and h < k and v[h+1][nx][ny] == INF:  # 벽이고 미방문
                    # 문 부수고 간다
                    v[h+1][nx][ny] = v[h][x][y] + 1
                    q.append((h+1, nx, ny))
                elif arr[nx][ny] == 0 and v[h][nx][ny] == INF: # 벽 아니고 미방문
                    # 문 안부수고 간다
                    v[h][nx][ny] = v[h][x][y] + 1
                    q.append((h, nx, ny))
    # 정답찾기
    mn = INF
    for h in range(0, k+1):
        if v[h][n-1][m-1] < mn:
            mn = v[h][n-1][m-1]
    if mn == INF:
        return -1
    else:
        return mn

n, m, k = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
ans = bfs()
print(ans)