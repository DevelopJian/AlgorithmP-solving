# BFS
import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())
maze = [list(map(int, input().rstrip())) for _ in range(n)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
q = deque([(0,0)]) # 시작점 넣기

while q :
    x, y = q.popleft()
    for dir in range(4):
        nx, ny = x + dx[dir], y + dy[dir]
        if 0 <= nx < n and 0 <= ny < m and maze[nx][ny] == 1:
            q.append((nx,ny))
            maze[nx][ny] = maze[x][y] + 1

print(maze[n-1][m-1])
