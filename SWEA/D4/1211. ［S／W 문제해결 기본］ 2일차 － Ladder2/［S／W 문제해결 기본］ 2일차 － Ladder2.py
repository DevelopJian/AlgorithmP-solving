for _ in range(10):
    tc = int(input())
    lad = [[0]+list(map(int, input().split()))+[0] for _ in range(100)]
    mn = 100*100+100

    for j in range(1, 101):
        if lad[0][j] == 0:
            continue

        x, y, dir, cnt = 0, j, 0, 0
        start = y - 1
        while x < 99:
            cnt += 1
            # 내려가던거
            if dir == 0:
                if lad[x][y-1] == 1: # 좌측 1
                    y = y-1
                    dir = -1
                elif lad[x][y+1] == 1: # 우측 1
                    y = y+1
                    dir = +1
                else :  # 좌우 1없으면 그대로 내려간다
                    x = x+1
            # 좌우로 가던거
            elif dir == -1 or dir == 1:
                if lad[x][y+dir] == 0:  # 0만나면 내려가는걸로 방향바꾼다
                    x = x+1
                    dir = 0
                else :  # 0안만나면 가던방향 그대로 간다
                    y = y+dir
        # 다내려가면
        if cnt < mn:
            mn = cnt
            result = start
            
    print(f'#{tc} {result}')