from collections import deque
inf = float('inf')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    # BFS
    q = deque([(0, 0)])
    v = [[inf] * n for _ in range(n)]  # inf == 미방문
    v[0][0] = 0

    while q:
        i, j = q.popleft()
        # 정답처리? -> 끝까지 다 돌아야하니까 필요없음
        for di, dj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < n:  # 1. 범위 내
                # 2. 갱신예정값이 더 작을 때 -> 갱신
                if v[i][j] + arr[ni][nj] < v[ni][nj]:
                    v[ni][nj] = v[i][j] + arr[ni][nj]
                    q.append((ni, nj))

    # 출발지 (0,0), 도착지(n-1, n-1)
    print(f'#{tc} {v[n - 1][n - 1]}')