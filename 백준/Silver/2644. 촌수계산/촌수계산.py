from collections import deque

def bfs(a, b): # 시작점, 도착점
    q = deque([a])
    v = [0]*(n+1)
    v[a] = 1
    while q:
        c = q.popleft()
        if c == b:
            break
        for nxt in rlt[c]:
            if v[nxt] == 0:
                q.append(nxt)
                v[nxt] = v[c] + 1
    return v[b]-1

n = int(input()) # 전체사람수
a, b = map(int, input().split()) # 촌수계산해야하는 사람
m = int(input())
rlt = [[] for _ in range(n+1)] # 양방향 연결리스트
for _ in range(m):
    x, y = map(int, input().split())
    rlt[x].append(y)
    rlt[y].append(x)

print(bfs(a,b))