t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = [0] * 201
    for _ in range(n):
        s, e = map(int, input().split())
        if s > e: # 순서가 바꿔서 들어올 수도 있음
            s, e = e, s
        for i in range((s-1)//2, (e-1)//2 +1):
            lst[i] += 1

    print(f'#{tc} {max(lst)}')
