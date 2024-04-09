from collections import deque
def bfs(si, sj, time):
    q = deque([(si, sj)])
    v = [[0] * (m+2) for _ in range(n+2)]
    v[si][sj] = 1
    cnt = 1 # 탈주범 갈 수 있는 곳 갯수
    move = {0:[1,2,5,6], 1:[1,2,4,7], 2:[1,3,4,5], 3:[1,3,6,7]} # 상0 하1 좌2 우3: 갈 수 있는 파이프번호
    di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
    while q:
        i, j = q.popleft()
        if v[i][j] >= time:
            break

        if arr[i][j] == 1: # 상하좌우
            lst = [0,1,2,3]
        elif arr[i][j] == 2:
            lst = [0, 1]
        elif arr[i][j] == 3:
            lst = [2, 3]
        elif arr[i][j] == 4:
            lst = [0, 3]
        elif arr[i][j] == 5:
            lst = [1, 3]
        elif arr[i][j] == 6:
            lst = [1, 2]
        elif arr[i][j] == 7:
            lst = [0, 2]

        for dir in lst:
            ni, nj = i + di[dir], j + dj[dir]
            if not v[ni][nj] and arr[ni][nj] in move[dir]:
                q.append((ni, nj))
                v[ni][nj] = v[i][j] + 1
                cnt += 1
    return cnt

t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split()) # 세로가로크기, 맨홀좌표, 시간
    arr = [[0] * (m+2)]+ [[0] + list(map(int, input().split())) + [0] for _ in range(n)] + [[0] * (m+2)]
    ans = bfs(r+1, c+1, l)
    print(f'#{tc} {ans}')