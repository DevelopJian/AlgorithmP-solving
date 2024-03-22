from collections import deque

def bfs(start):
    q = deque([start])

    while q:
        now = q.popleft()

        for nxt in rel[now]:
            if not v[nxt]:
                v[nxt] = 1
                q.append(nxt)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 사람 1~n번
    rel = [[] for _ in range(n+1)]
    for _ in range(m):
        a, b = map(int, input().split())
        rel[a].append(b) # 양방향
        rel[b].append(a)

    v = [0] * (n+1)
    ans = 0

    for i in range(1, n+1):
        if not v[i]:
            ans += 1
            bfs(i)

    print(f'#{tc} {ans}')