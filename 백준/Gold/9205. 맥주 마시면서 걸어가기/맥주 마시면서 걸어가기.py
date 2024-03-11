from collections import deque
def bfs(si, sj, ei, ej):
    q = deque([(si, sj)])
    v = [0] * n  # 편의점 방문표시
    while q:
        i, j = q.popleft()
        # 정답처리
        if abs(ei-i) + abs(ej-j) <= 1000:
            return 'happy'

        # q에 넣기 (미방문, 거리가 1000 이하)
        for c in range(n):
            if not v[c]:
                ni, nj = cnv[c]
                if abs(ni-i) + abs(nj-j) <= 1000:
                    v[c] = 1
                    q.append((ni, nj))
    return 'sad'


t = int(input())
for _ in range(t):
    n = int(input()) # 편의점 수
    si, sj = map(int, input().split())
    cnv = []
    for _ in range(n):
        i, j = map(int, input().split())
        cnv.append((i, j))
    ei, ej = map(int, input().split())

    print(bfs(si, sj, ei, ej))
