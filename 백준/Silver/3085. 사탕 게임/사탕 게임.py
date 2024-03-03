n = int(input())
arr = [list(input()) for _ in range(n)]
arr2 = list(map(list, zip(*arr)))

mx = 1
for i in range(n):
    for j in range(1, n):
        # 가로 다른것들끼리만 변경
        if arr[i][j] == arr[i][j-1]:
            continue
        arr[i][j], arr[i][j-1] = arr[i][j-1], arr[i][j]
        # 가로 확인
        for x in range(n):
            sm = 1
            for y in range(1,n):
                if arr[x][y] == arr[x][y-1]:
                    sm += 1
                else:
                    sm = 1
                mx = max(mx, sm)
        # 세로확인(전치행렬)
        tp = list(map(list, zip(*arr)))
        for x in range(n):
            sm = 1
            for y in range(1,n):
                if tp[x][y] == tp[x][y-1]:
                    sm += 1
                else:
                    sm = 1
                mx = max(mx, sm)
        arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]

for i in range(n):
    for j in range(1, n):
        # 가로 다른것들끼리만 변경
        if arr2[i][j] == arr2[i][j-1]:
            continue
        arr2[i][j], arr2[i][j-1] = arr2[i][j-1], arr2[i][j]
        # 가로 확인
        for x in range(n):
            sm = 1
            for y in range(1,n):
                if arr2[x][y] == arr2[x][y-1]:
                    sm += 1
                else:
                    sm = 1
                mx = max(mx, sm)
        # 세로확인(전치행렬)
        tp = list(map(list, zip(*arr2)))
        for x in range(n):
            sm = 1
            for y in range(1,n):
                if tp[x][y] == tp[x][y-1]:
                    sm += 1
                else:
                    sm = 1
                mx = max(mx, sm)
        arr2[i][j], arr2[i][j - 1] = arr2[i][j - 1], arr2[i][j]
print(mx)