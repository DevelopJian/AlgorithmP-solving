t = int(input())
for tc in range(1, t+1):
    n, m = map(int, input().split()) # 도시크기(5~20), 한집당 지불비용
    arr = [list(map(int, input().split())) for _ in range(n)] # 1 : 집 위치한 곳 (최소 1개)
    homes = []
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                homes.append((i, j))

    mxhome = 1  # 손해 안보고 서비스 받을 수 있는 집 최대값 (k=1 이면 항상 한 집에 서비스 줄 수 있고 손해 안봄)

    for i in range(n):  # 중심 : (x, y)
        for j in range(n):
            x, y = i, j

            nums = [0] * 39
            for nx, ny in homes:
                nums[abs(nx-x) + abs(ny-y)] += 1

            for d in range(2*n-2, -1, -1):
                avahome = sum(nums[0:d+1])
                # 손해여부 확인
                if avahome * m >= (d+1)*(d+1) + d*d:  # 지불비용 >= 드는비용  == 손해 안본다 -> break
                    break

            if mxhome < avahome:
                mxhome = avahome
    print(f'#{tc} {mxhome}')