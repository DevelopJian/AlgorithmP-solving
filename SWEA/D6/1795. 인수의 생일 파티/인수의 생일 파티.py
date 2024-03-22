from collections import deque
inf = float('inf')

def bfs(sn, en):
    go = back = inf # 가는길, 오는길 최소값으로 갱신예정

    # 1. 가는길 최소값 구하기
    q = deque([(sn, 0)]) # (현재노드, 지금까지 걸린시간)
    v = [inf] * (n+1)
    v[sn] = 0

    while q:
        now, time = q.popleft()
        # 정답갱신
        if now == en:
            go = min(go, time)
            continue
        # q에 넣기
        for nxt, t in adj[now]:
            newtime = time + t
            if newtime < v[nxt]:
                v[nxt] = newtime
                q.append((nxt, newtime))

    # 2. 오는길 최소값 구하기
    q = deque([(en, 0)])  # (현재노드, 지금까지 걸린시간)
    v = [inf] * (n + 1)
    v[en] = 0

    while q:
        now, time = q.popleft()
        # 정답갱신
        if now == sn:
            back = min(back, time)
            continue
        # q에 넣기
        for nxt, t in adj[now]:
            newtime = time + t
            if newtime < v[nxt]:
                v[nxt] = newtime
                q.append((nxt, newtime))

    return go + back

t = int(input())
for tc in range(1, t+1):
    n, m, x = map(int, input().split())  # 집 갯수, 간선갯수, x번집 오고가기

    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        s, e, l = map(int, input().split())
        adj[s].append((e, l))

    # 1. 각 노드 마다 최단 시간 구하고 2. 그 중 가장 큰 것 = ans
    time = [0] * (n+1)

    for node in range(1, n+1):
        if node == x:
            continue
        mn = bfs(node, x)
        time[node] = mn

    print(f'#{tc} {max(time)}')