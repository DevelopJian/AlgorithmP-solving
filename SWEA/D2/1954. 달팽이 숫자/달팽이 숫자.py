t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [[0]*n for _ in range(n)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    x, y, dir, num = 0, 0, 0, 1 # 초기화
    lst[x][y] = num
    num += 1

    while num <= n**2:
        nx, ny = x+dx[dir], y+dy[dir]
        if 0<= nx <n and 0<= ny <n and lst[nx][ny] == 0:
            x, y = nx, ny
            lst[x][y] = num
            num += 1
        else:
            dir = (dir+1) % 4

    print(f'#{tc}')
    for l in lst:
        print(*l)