import sys
input = sys.stdin.readline
from collections import deque
# 작은번호부터 방문 -> 함수로하는게 순서대로 하니까 더 나을듯
def dfs(start):
    dvisited[start] = 1 # 방문했으니 바로 출력
    print(start, end =' ')
    for next in nodes[start]:
        if not dvisited[next]:
            dfs(next)
def bfs(start):
    que = deque([start])
    bvisited[start] = 1 # 큐에 넣었으니 방문한걸로 바꾸기
    while que :
        now = que.popleft()
        print(now, end = ' ')
        for next in nodes[now]:
            if not bvisited[next]:
                que.append(next)
                bvisited[next] =1
# 큐에 들어가있는 숫자는 아직 visit하지 않은 것이 되니까 뒤에서 중복되면 계속 중복으로 들어감.
# 그래서 큐에 넣을 때 바로 visit한걸로 바꿔줘야함

n, m, v = map(int, input().split())
nodes = [[] for _ in range(n+1)]
dvisited = [0] * (n+1)  # 0= 방문안함, 1= 방문함
bvisited = [0] * (n+1)
for _ in range(m):
    s, e = map(int, input().split())
    nodes[s].append(e)
    nodes[e].append(s) # 양방향으로 추가
for lst in nodes :
    lst.sort()
dfs(v)
print()
bfs(v)