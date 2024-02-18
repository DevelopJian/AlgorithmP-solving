# BFS로 푸는 방법
import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip()) # 노드수
v = int(input().rstrip()) # 엣지수
cpt = [[] for _ in range(n+1)]
for _ in range(v):
    s, e = map(int, input().split())
    cpt[s].append(e)
    cpt[e].append(s)  # 양방향 추가

que = deque([1])
visited = [0] * (n+1)
visited[1] = 1
cnt = 0 # 1번컴퓨터 빼고
while que :
    start = que.popleft()
    for nd in cpt[start]:
        if not visited[nd]:
            que.append(nd)
            visited[nd] = 1
            cnt += 1
print(cnt)