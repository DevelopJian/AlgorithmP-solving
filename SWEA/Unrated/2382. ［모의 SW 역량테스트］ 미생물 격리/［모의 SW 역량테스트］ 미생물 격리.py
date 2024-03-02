t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split()) # 가로세로갯수, 시간, 군집수
    dx, dy = [0,-1,1,0,0], [0,0,0,-1,1]
    tbl = [0,2,1,4,3]
    arr = [list(map(int, input().split())) for _ in range(k)]

    for _ in range(m):
        # 이동시킴
        for row in range(len(arr)):
            arr[row][0], arr[row][1] = arr[row][0]+dx[arr[row][3]], arr[row][1]+dy[arr[row][3]]
            if arr[row][0] == 0 or arr[row][0] == n-1 or arr[row][1] == 0 or arr[row][1] == n-1: # 경계선이면
                arr[row][2] = arr[row][2]//2  # 갯수 나눠줌
                arr[row][3] = tbl[arr[row][3]]

        # 내림차순정렬
        arr.sort(key = lambda x : (x[0],x[1],x[2]), reverse=True)

        # 같은좌표 합해주기
        row = 1
        while row <len(arr):
            if arr[row][0] == arr[row-1][0] and arr[row][1] == arr[row-1][1]:
                arr[row-1][2] += arr[row][2]
                arr.pop(row)
            else:
                row += 1

    ans = 0
    for lst in arr:
        ans += lst[2]

    print(f'#{tc} {ans}')