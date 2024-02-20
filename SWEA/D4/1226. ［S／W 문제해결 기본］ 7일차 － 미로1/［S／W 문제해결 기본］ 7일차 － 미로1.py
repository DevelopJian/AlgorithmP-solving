def dfs(x, y):
    for dx, dy in ((0, 1), (1, 0), (-1, 0), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < 16 and 0 <= ny < 16 and maze[nx][ny] != 1:
            maze[nx][ny] = 1
            dfs(nx, ny)

for _ in range(10):
    tc = input()
    maze = [list(map(int, input())) for _ in range(16)]
    # 시작, 도착점 찾기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                sx, sy = i, j
            if maze[i][j] == 3:
                ex, ey = i, j

    dfs(sx, sy)
    print(f'#{tc} {1 if maze[ex][ey] == 1 else 0}')