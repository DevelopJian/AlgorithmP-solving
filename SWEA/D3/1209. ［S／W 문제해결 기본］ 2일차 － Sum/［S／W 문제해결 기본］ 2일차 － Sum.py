for _ in range(1, 11):
    tc = input()
    arr = [list(map(int, input().split())) for _ in range(100)]
    arr2 = list(zip(*arr))
    mx = 0
    for row in range(100):
        mx = max(mx, sum(arr[row]), sum(arr2[row]))
    sm = 0
    for i in range(100):
        sm += arr[i][i]
    mx = max(sm, mx)
    sm = 0
    for i in range(100):
        sm += arr[i][99-i]
    mx = max(sm, mx)
    print(f'#{tc} {mx}')