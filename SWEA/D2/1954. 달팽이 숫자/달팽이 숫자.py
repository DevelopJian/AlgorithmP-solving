t = int(input())
for tc in range(1, 1+t):
    n = int(input())
    arr = [[0]*n for _ in range(n)]
    # 칸이 없거나 0이면 방향바꾸기
    dx, dy = [0,1,0,-1],[1,0,-1,0]
    dr = 0
    x, y = 0, 0
    for num in range(1, n**2+1):
        arr[x][y] = num
        nx, ny = x+dx[dr], y+dy[dr]
        if 0<=nx<n and 0<=ny<n and arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            dr = (dr+1)%4
            x, y = x + dx[dr], y + dy[dr]

    print(f'#{tc}')
    for l in arr:
        print(*l)