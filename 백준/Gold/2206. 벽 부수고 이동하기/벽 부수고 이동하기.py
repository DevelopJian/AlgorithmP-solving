from collections import deque
def bfs(ei, ej): # 도착점
    global mn
    q = deque([(0, 0, 0)]) # ck(벽), ci, cj
    v = [[[0]*m for _ in range(n)] for _ in range(2)]
    v[0][0][0] = 1

    while q:
        ck, ci, cj = q.popleft()
        # 정답처리
        if ci == ei and cj == ej: # 도착점에 도달했다면
            mn = min(mn, v[ck][ci][cj])

        # q에 넣기
        for di, dj in ((-1,0),(1,0),(0,1),(0,-1)):
            ni, nj = ci+di, cj+dj
            if 0<= ni < n and 0 <= nj < m: # 사방 범위 내
                if arr[ni][nj] == 0 and not v[ck][ni][nj]: # 벽 아니고, 방문 안했으면
                    v[ck][ni][nj] = v[ck][ci][cj] + 1
                    q.append((ck, ni, nj))
                elif arr[ni][nj] == 1 and not v[ck][ni][nj] and ck == 0: # 벽이고, 방문 안했고, 벽 안뚫었다면
                    if ck == 0: # 벽 안뚫었다면
                        v[1][ni][nj] = v[0][ci][cj] + 1
                        q.append((1, ni, nj))
    # 가능한 곳 다 갔는데도 도착점 도달 못했다면
    if mn == 1000*1000*2:
        mn = -1
    return

n, m = map(int, input().split())
arr = [list(map(int, input())) for _ in range(n)]
mn = 1000*1000*2
bfs(n-1, m-1)

print(mn)