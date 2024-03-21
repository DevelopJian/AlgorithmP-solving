from collections import deque

def bfs(s):
    q = deque([s])

    while q:
        now = q.popleft()
        for node in lst[now]:
            if not v[node]:
                v[node] = 1
                q.append(node)

t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 사람 수, 연결 수
    ipt = list(map(int, input().split()))
    lst = [[] for _  in range(n+1)] # 인접리스트 (양방향)

    for i in range(0, 2*m, 2):
        lst[ipt[i]].append(ipt[i+1])
        lst[ipt[i+1]].append(ipt[i])
    v = [0] * (n+1)
    ans = 0
    for i in range(1, n+1):
        if not v[i]:
            ans += 1  # bfs 함수 호출횟수
            v[i] = 1
            bfs(i)

    print(f'#{tc} {ans}')