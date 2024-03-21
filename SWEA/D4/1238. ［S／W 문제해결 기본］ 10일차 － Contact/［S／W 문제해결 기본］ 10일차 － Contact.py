from collections import deque

def bfs(start):
    q = deque([(0, start)])  # (연락순서, 시작점)
    v = [0] * 101
    v[start] = 1

    mxtime = mxnode = 0

    while q:
        time, now = q.popleft()
        # 같은 레벨 중 최대노드 갱신
        if mxtime < time:
            mxtime, mxnode = time, now
        elif mxtime == time:
            mxnode = max(mxnode, now)
        for node in nodes[now]:
            if not v[node]:
                v[node] = 1
                q.append((time + 1, node))
    return mxnode

t = 10
for tc in range(1, t+1):
    n, start = map(int, input().split())
    nodes = [[] for _ in range(101)]  # 인접 리스트

    arr = list(map(int, input().split()))
    for i in range(0, n, 2):
        nodes[arr[i]].append(arr[i+1])

    ans = bfs(start)

    print(f'#{tc} {ans}')