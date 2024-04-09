import sys
input = sys.stdin.readline

r, c, t = map(int, input().split()) # 세로, 가로, 초 (과정을 t번 해야함)
arr = [list(map(int, input().split())) for _ in range(r)]
machine = [] # 청정기 좌표 ([0]:위, [1]:아래)
for k in range(r):
        if arr[k][0] == -1:
            arr[k][0] = 0
            machine.append((k, 0))
ux, uy, lx, ly = machine[0][0], 0, machine[1][0], 0

for _ in range(t): # t번 반복
    temp = [[0]*c for _ in range(r)]
    # 확산: Temp에 저장, 본인: 확산된만큼 빼기
    for i in range(r):
        for j in range(c):
            if arr[i][j] == 0:
                continue
            diff = arr[i][j] // 5 # 확산할 양
            if diff == 0:
                continue
            cnt = 0 # 확산할 칸 갯수
            for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
                ni, nj = i + di, j + dj
                if 0<= ni < r and 0 <= nj < c and (ni, nj) not in machine: # 1. 범위내, 2. 청정기 아니라면
                    cnt += 1
                    temp[ni][nj] += diff
            arr[i][j] -= (diff * cnt)
    # 확산받은 양 더해주기
    for i in range(r):
        for j in range(c):
            arr[i][j] += temp[i][j]
    # 위쪽 청정기 순환
    di, dj = [-1, 0, 1, 0], [0, 1, 0, -1]
    dir = 0
    x, y = ux-1, uy
    while True:
        if 0<= x+di[dir] <= ux  and 0<= y+dj[dir] < c: # 범위내라면 방향 그대로
            arr[x][y] = arr[x+di[dir]][y+dj[dir]]
        else: # 범위밖이라면 방향 바꾸기
            dir += 1
            if dir == 4:
                break
            arr[x][y] = arr[x + di[dir]][y + dj[dir]]
        x, y = x + di[dir], y + dj[dir]
    # 아래쪽 청정기 순환
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    dir = 0
    x, y = lx+1, ly
    while True:
        if lx<= x+di[dir] < r  and 0<= y+dj[dir] < c: # 범위내라면 방향 그대로
            arr[x][y] = arr[x+di[dir]][y+dj[dir]]
        else: # 범위밖이라면 방향 바꾸기
            dir += 1
            if dir == 4:
                break
            arr[x][y] = arr[x + di[dir]][y + dj[dir]]
        x, y = x + di[dir], y + dj[dir]
    # 청정기 0으로 바꿔주기
    arr[ux][uy], arr[lx][ly] = 0, 0
ans = 0
for lst in arr:
    ans += sum(lst)
print(ans)