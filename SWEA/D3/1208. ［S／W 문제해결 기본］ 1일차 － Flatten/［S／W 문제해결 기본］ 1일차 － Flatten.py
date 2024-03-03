for tc in range(1, 11):
    # 가로길이 100
    n = int(input())
    h = list(map(int, input().strip().split()))
    for i in range(n):
        h.sort()
        if h[-1] - h[0] <= 1 :
            break
        else:
            h[-1] -= 1
            h[0] += 1
    print(f'#{tc} {max(h) - min(h)}')
