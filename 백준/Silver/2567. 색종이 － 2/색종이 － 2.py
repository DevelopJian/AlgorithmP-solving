n = int(input())

arr = [[0]*102 for _ in range(102)]
for _ in range(n):
    x, y = map(int, input().split())
    for i in range(x, x+10):
        for j in range(y, y+10):
            arr[i][j] = 1
cnt = 0
for i in range(101):
    for j in range(101):
        if arr[i][j] != arr[i+1][j] :
            cnt += 1
        if arr[i][j] != arr[i][j+1]:
            cnt += 1
print(cnt)
