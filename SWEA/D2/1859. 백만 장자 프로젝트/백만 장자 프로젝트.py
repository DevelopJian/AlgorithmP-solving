t = int(input())
for tc in range(1,t+1):
    n = int(input())
    price = list(map(int, input().split()))
    mx = 0
    sm = 0
    for p in price[::-1]:
        # mx보다 큰거나오면
        if p >= mx:
            mx = p
        # mx보다 작은거 나오면
        else:
            sm += (mx - p)

    print(f'#{tc} {sm}')