t = int(input())
for tc in range(1,t+1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    flag = True
    # 가로검증
    for row in arr:
        if len(row) != len(set(row)):
            flag = False
            break
    # 세로검증
    arr2 = list(zip(*arr)) # 전치행렬
    for row in arr2:
        if len(row) != len(set(row)):
            flag = False
            break
    # 박스검증
    for i in range(0,9,3): # 012 345 678
        for j in range(0,9,3):
            temp = []
            for dx, dy in ((0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)):
                temp.append(arr[i+dx][j+dy])
            if len(temp) != len(set(temp)):
                flag = False
                break
    print(f'#{tc} {1 if flag else 0}')