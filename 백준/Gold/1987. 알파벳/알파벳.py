import sys
input = sys.stdin.readline

def dfs(cnt, x, y): # 방문한 칸수, 이전좌표
    global mx
    if cnt > mx:
        mx = cnt
    # 사방탐색
    for dx, dy in ((0,1),(1,0),(0,-1),(-1,0)):
        nx, ny = x+dx, y+dy
        # 1. 범위 내 2. 같은 알파벳 아닐 때 (지나온 칸은 어차피 알파벳 중복이니 칸에대한 visit 체크 필요없음)
        if 0<= nx < r and 0<= ny < c and not alph[ord(arr[nx][ny]) - 65]: # 아스키코드 이용
            alph[ord(arr[nx][ny]) - 65] = 1
            dfs(cnt + 1, nx, ny)
            alph[ord(arr[nx][ny]) - 65] = 0

r, c = map(int, input().strip().split())
arr = [list(input().strip()) for _ in range(r)]
alph = [0]*26
alph[ord(arr[0][0]) - 65] = 1
mx = 0

dfs(1, 0, 0)

print(mx)