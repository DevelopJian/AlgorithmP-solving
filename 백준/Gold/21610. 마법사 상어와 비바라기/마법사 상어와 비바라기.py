n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)] # n*n
dx, dy = [100, 0, -1, -1, -1, 0, 1, 1, 1], [100, -1, -1, 0, 1, 1, 1, 0, -1] # 1번부터 사용
cloud = [(n-1, 0),(n-1, 1),(n-2, 0),(n-2, 1)]
for _ in range(m):
    move = []
    dir, num = map(int, input().split()) # 방향, 이동길이
    num = num % n
    while cloud:
        x, y = cloud.pop()
        nx, ny = (x + dx[dir]*num) % n, (y + dy[dir]*num) % n
        move.append((nx, ny))
        arr[nx][ny] += 1
    for i, j in move:
        cnt = 0
        for di, dj in ((-1, -1),(-1, 1),(1, -1), (1, 1)):
            ni, nj = i + di, j + dj
            if 0<= ni < n and 0<= nj <n and arr[ni][nj] > 0:
                cnt += 1
        arr[i][j] += cnt
    for r in range(n):
        for c in range(n):
            if arr[r][c] >= 2 and (r, c) not in move:
                cloud.append((r, c))
                arr[r][c] -= 2
ans = 0
for lst in arr:
    ans += sum(lst)
print(ans)