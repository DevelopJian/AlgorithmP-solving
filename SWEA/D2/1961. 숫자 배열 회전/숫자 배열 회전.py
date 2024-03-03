t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    arr2 = list(zip(*reversed(arr)))
    arr3 = list(zip(*reversed(arr2)))
    arr4 = list(zip(*reversed(arr3)))
    print(f'#{tc}')
    for i in range(n):
        print(*arr2[i], sep='', end= ' ')
        print(*arr3[i], sep='', end=' ')
        print(*arr4[i], sep='')
