from collections import deque
def move():
    movebool = False
    v = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if not v[i][j]:
                v[i][j] = 1
                if bfs(i, j, v):
                    movebool = True
    return movebool

def bfs(si, sj, v):
    temp = [(si, sj)] # 이동할 리스트
    sm = arr[si][sj] # 이동할 리스트 인구 합
    q = deque([(si, sj)])
    while q:
        i, j = q.popleft()
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = i + di, j + dj
            if 0<=ni<n and 0<=nj<n and not v[ni][nj]:
                if l <= abs(arr[i][j] - arr[ni][nj]) <= r:
                    v[ni][nj] = 1
                    temp.append((ni, nj))
                    q.append((ni, nj))
                    sm += arr[ni][nj]
    # 이동안한다면
    if len(temp) <= 1:
        return False
    # 이동한다면 => 이동시키기
    num = sm // len(temp)
    for x, y in temp:
        arr[x][y] = num
    return True

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
day = 0
while True:
    if move():
        day +=1
    else:
        break

print(day)