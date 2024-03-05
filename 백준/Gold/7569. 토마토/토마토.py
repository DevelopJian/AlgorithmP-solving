from collections import deque

m, n, height = map(int, input().split()) #상자 가로세로, 상자수(높이)
arr = [list(map(int, input().split())) for _ in range(n*height)]

def bfs():
    q = deque()
    # q에 초기값(익은것) 넣어주기
    for i in range(n * height):
        for j in range(m):
            if arr[i][j] == 1:
                q.append((i, j))

    if len(q) == m*n*height: # 모두 익어있는 경우
        return 0
    elif len(q) == 0: # 초기에 익은게 하나도 없는 경우
        return -1

    while q:
        x, y = q.popleft()

        # 사방에 있는 것 넣기
        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x+dx, y+dy
            if (x//n) * n <= nx < (x//n) * n + n and 0<= ny < m and arr[nx][ny] == 0:  # 그 층 바깥으로 나가지 않도록 확인
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))
        # 위아래 넣기
        for h in (-1,1):
            nx, ny = x + n*h, y
            if 0<= nx < n*height and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))

    # 익지않은게 있는지 확인 & 답구해주기
    days = 0
    for i in range(n * height):
        for j in range(m):
            if arr[i][j] == 0:
                return -1
            days = max(days, arr[i][j])

    return days - 1 # 1부터 시작했기 때문에 1 빼줌

print(bfs())