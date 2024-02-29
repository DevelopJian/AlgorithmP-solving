dct = {} # 값 : 좌표
rdct = {} # 좌표 : 값
x, y = 1, 1
for num in range(1, 500000):
    dct[num] = (x, y)
    rdct[(x, y)] = num
    x, y = x+1, y-1
    if y < 1:
        x, y = 1, x

t = int(input())
for tc in range(1, t+1):
    p, q = map(int, input().split())
    px, py = dct[p]
    qx, qy = dct[q]

    ans = rdct[px+qx, py+qy]
    print(f'#{tc} {ans}')