from collections import deque
import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = [list(map(int, input().rstrip())) for _ in range(n)]
homecnt = []
# 출발점 찾아서 BFS로 탐색 -> 다했으면 다시 출발점 찾기
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    for j in range(n):
        # 출발점 찾기
        if lst[i][j] == 1:
            que = deque([(i,j)])
            lst[i][j] = 0 # 방문할곳 체크
            cnt = 1
            while que :
                now_x, now_y = que.popleft()
                for dir in range(4):
                    next_x, next_y = now_x+dx[dir], now_y+dy[dir]
                    if 0<= next_x <n and 0<=next_y <n and lst[next_x][next_y] == 1:
                        que.append((next_x, next_y))
                        lst[next_x][next_y] = 0
                        cnt += 1
            homecnt.append(cnt)
homecnt.sort()
print(len(homecnt))
print(*homecnt, sep='\n')