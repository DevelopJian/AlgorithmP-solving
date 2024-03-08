# 비 높이 : 0 ~ (최대 수 -1) 까지 확인하기
# 전체 순회, 비높이보다 높은지역 있다면 시작점.상하좌우 중 비높이보다 높은 점 큐에 다 넣기
# 비높이보다 높은지역만 골라서 순회 -> start 갯수의 최대 찾기

from collections import deque
def bfs(si, sj):
    q = deque([(si, sj)])
    while q:
        x, y = q.popleft()
        for dx, dy in ((-1, 0),(1,0),(0,-1),(0,1)):
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0<= ny < n and lst[nx][ny] > rain and not v[nx][ny]:
                v[nx][ny] = 1
                q.append((nx, ny))

n = int(input()) # 가로세로
lst = [list(map(int, input().split())) for _ in range(n)]

ans = 0
high = 0 # 제일 높은 곳
for i in range(n):
    for j in range(n):
        high = max(high, lst[i][j])

rain = 0
while rain < high:
    start = 0
    v = [[0]*n for _ in range(n)]
    # 시작점찾기
    for i in range(n):
        for j in range(n):
            if lst[i][j] > rain and not v[i][j]:
                start += 1
                v[i][j] = 1
                bfs(i, j)
    ans = max(ans, start)
    rain += 1

print(ans)