for _ in range(10):
    tc = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    # 도착점찾기 -> 도착점에서 위로 올라가서 출발점 찾기
    for i in range(100):
        if ladder[99][i] == 2:
            break
    x, y = 99, i

    while x != 0:
        for dx, dy in ((0, -1), (0, 1), (-1, 0)): # 좌 우 상
            if 0<= x+dx<100 and 0<= y+dy <100 and ladder[x+dx][y+dy] == 1:
                ladder[x][y] = 0
                x, y = x+dx, y+dy
                break

    print(f'#{tc} {y}')