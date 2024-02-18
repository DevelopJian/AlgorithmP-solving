from collections import deque
# BFS
def bfs():
    q = deque()
    q.append(n)
    while q :
        now = q.popleft()
        if now == k :
            print(road[k])
            break
        for next in (now-1, now+1, now*2):
            if 0<= next <= 10**5 and not road[next]:
                road[next] = road[now] + 1
                q.append(next)

n, k = map(int, input().split())
road = [0] * (10**5+1)
bfs()