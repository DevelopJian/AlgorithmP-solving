t= int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [tuple(map(int, input().split())) for _ in range(n)]
    lst.sort(key = lambda x : x[1])

    ans = 0
    last = 0
    for s, e in lst:
        if last<= s:
            ans += 1
            last = e
            
    print(f'#{tc} {ans}')