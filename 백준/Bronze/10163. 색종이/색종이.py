n = int(input()) # 색종이장수
# 좌표 너비 높이
arr = [[0]*1001 for _ in range(1001)]
for c in range(1, n+1):
    x, y, w, h = map(int, input().split())
    for i in range(x, x+w):
        for j in range(y, y+h):
            arr[i][j] = c

for c in range(1, n+1):
    cnt = 0
    for row in range(1001):
        cnt += arr[row].count(c)
    print(cnt)