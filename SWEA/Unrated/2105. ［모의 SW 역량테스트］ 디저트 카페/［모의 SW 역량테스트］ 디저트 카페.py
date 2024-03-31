di = [1, 1, -1, -1]
dj = [1, -1, -1, 1]

def dfs(si, sj, i, j, cnt, dir): # 시작점, 현재점, 디저트먹은 수(시작점 뺀거), 방향
    global mx
    # 정답처리
    if si == i and sj == j and dir == 3:
        if cnt > mx:
            mx = cnt
        return
    # 함수호출

    # 방향 안바꾸기
    ni, nj = i + di[dir], j + dj[dir]
    if 0 <= ni < n and 0<=nj < n and not v[arr[ni][nj]]:  # 범위 내, 미방문
        v[arr[ni][nj]] = 1
        dfs(si, sj, ni, nj, cnt + 1, dir)
        v[arr[ni][nj]] = 0

    # 방향 바꾸기
    if dir < 3:
        ni, nj = i + di[dir+1], j + dj[dir+1]
        if 0<= ni <n and 0<= nj < n and not v[arr[ni][nj]]: # 범위 내, 미방문
            v[arr[ni][nj]] = 1
            dfs(si, sj, ni, nj, cnt + 1, dir + 1)
            v[arr[ni][nj]] = 0

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    mx = -1
    for i in range(n-2):
        for j in range(1, n-1):
            v = [0] * 101
            v[arr[i+1][j+1]] = 1
            dfs(i, j, i+1, j+1, 1, 0)

    print(f'#{tc} {mx}')