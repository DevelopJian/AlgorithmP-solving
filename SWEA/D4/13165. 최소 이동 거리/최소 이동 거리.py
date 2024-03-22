from collections import deque
inf = float('inf')
 
def bfs(start):
    q = deque([(start, 0)])  # (노드번호, 지금까지 간 거리)
    v = [inf] * (N+1)
    v[start] = 0
 
    while q:
        node, dst = q.popleft()
        for nxt, d in lst[node]:
            newdst = dst + d
            if newdst < v[nxt]:  # 새 거리가 저장돼있던 거리보다 작다면 갱신
                v[nxt] = newdst
                q.append((nxt, newdst))
 
    return v[N]
 
t = int(input())
for tc in range(1, t+1):
    N, E = map(int, input().split())  # 노드 N+1개, 간선 E개
    lst = [[] for _ in range(N+1)] # 인접리스트
    for _ in range(E):
        s, e, w = map(int, input().split())
        lst[s].append((e, w))
 
    print(f'#{tc} {bfs(0)}')