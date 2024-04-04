di, dj = [-1, 0, 1, 0], [0, 1, 0, -1] # 상 좌 하 우
def move(si, sj, dir):
    i, j, d = si, sj, dir
    cnt = 0
    while True:
        # 1. 현재칸 청소안돼있다면 청소 -> 2번으로 넘어감
        if arr[i][j] == 0:
            arr[i][j] = 2
            cnt += 1
        # 2. 현재칸 청소 돼있다면 반시계방향으로 확인
        if arr[i][j] == 2:
            flag = False
            for num in range(3, -1, -1):
                drt = (d+num) % 4 # 현재 방향의 반시계 방향
                ni, nj = i + di[drt], j + dj[drt]
                # 청소안된 칸 있다면 거기로 가고, d를 그 방향으로 바꾸기(전진이라서), 그 칸 청소하기
                if arr[ni][nj] == 0:
                    i, j, d = ni, nj, drt
                    arr[i][j] = 2
                    cnt += 1
                    flag = True
                    break
            if flag: # 청소 안된 칸 있어서 갔다면
                continue
            else: # 청소 안된 칸 없었다면 -> 후진
                ni, nj = i + di[(d+2)%4], j + dj[(d+2)%4] # 후진하는 칸
                # 후진하는 칸이 벽이아니라면 거기로 이동, d는 같음(후진이라서)
                if arr[ni][nj] != 1:
                    i, j = ni, nj
                # 후진하는 칸이 벽이라면 -> return
                else:
                    return cnt

n, m = map(int, input().split())
si, sj, dir = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = move(si, sj, dir)
print(ans)