from collections import deque
def bfs(si, sj):
    q = deque([(si, sj)])
    mnroom = arr[si][sj]
    move = 0

    while q:
        x, y = q.popleft()
        mnroom = min(mnroom, arr[x][y])
        move += 1

        for dx, dy in ((1,0),(-1,0),(0,1),(0,-1)):
            nx, ny = x + dx, y + dy
            if 0<= nx < n and 0 <= ny < n and not v[nx][ny]:
                if abs(arr[nx][ny] - arr[x][y]) == 1:
                    v[nx][ny] = 1
                    q.append((nx, ny))
    return move, mnroom

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    v = [[0]*n for _ in range(n)]

    mxmove = start = 0
    for i in range(n):
        for j in range(n):
            if v[i][j]:
                continue
            v[i][j] = 1
            move, mnroom = bfs(i, j)
            if move == mxmove:
                start = min(mnroom, start)
            elif move > mxmove:
                mxmove = move
                start = mnroom

    print(f'#{tc} {start} {mxmove}')