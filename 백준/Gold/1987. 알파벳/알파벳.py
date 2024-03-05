import sys
input = sys.stdin.readline

def dfs(cnt, x, y): # 방문한 칸수, 이전좌표
    global mx
    if cnt > mx:
        mx = cnt
    # 사방탐색
    for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
        nx, ny = x+dx, y+dy
        if not v[nx][ny] and not alph[ord(arr[nx][ny]) - 65]: # 아스키코드 이용
            v[nx][ny] = 1
            alph[ord(arr[nx][ny]) - 65] = 1
            dfs(cnt + 1, nx, ny)
            v[nx][ny] = 0
            alph[ord(arr[nx][ny]) - 65] = 0

r, c = map(int, input().split())
arr = [[0]*(c+2)] + [[0]+list(input())+[0] for _ in range(r)] + [[0]*(c+2)]
# visit 배열 : 가장자리 미리 visit 처리(범위체크 필요없게)
v = [[1]*(c+2)] + [[1] + [0]*c + [1] for _ in range(r)] + [[1]*(c+2)]
v[1][1] = 1
alph = [0]*26
alph[ord(arr[1][1]) - 65] = 1
mx = 0

dfs(1, 1, 1)

print(mx)