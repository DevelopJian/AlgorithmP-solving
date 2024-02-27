t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split()) # n명, m초에 k개붕어빵
    lst = sorted(list(map(int, input().split())))

    sm = 0 # 지금까지 손님에게 준 + 지금 줄 붕어빵 수
    ans = 'Possible'

    for sec in lst:
        sm += 1
        if sec//m * k < sm:
            ans = 'Impossible'
            break
            
    print(f'#{tc} {ans}')