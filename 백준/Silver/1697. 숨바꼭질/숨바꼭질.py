from collections import deque
def bfs():
    q = deque()
    q.append(n)
    while q:
        now = q.popleft()
        if now == k:
            print(road[k]-1)  # 시작점 표시했던 것 하나 빼기
            break
        for next in (now * 2, now - 1, now + 1):
            if 0 <= next <= 10 ** 5 and not road[next]:
                road[next] = road[now] + 1
                q.append(next)


n, k = map(int, input().split())
road = [0] * (10 ** 5 + 1)
## 시작점 표시!!!(0에서 시작한다면 *2하면 0이 되기 때문에 1로 미리 바꿔주기)
road[n] = 1
bfs()
