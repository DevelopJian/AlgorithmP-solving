col, row = map(int, input().split()) # 갯수
k = int(input())
lst = [[0]*col for _ in range(row)]
flag = True

if col * row < k:
    flag = False

if flag:
    # dir = 상 우 하 좌 반복
    dirx = [-1, 0, 1, 0]
    diry = [0, 1, 0, -1]
    x, y, dir, dx, dy = row-1, 0, 0, -1, 0
    for num in range(1, k+1): # num = 적을 숫자
        lst[x][y] = num
        if num == k:
            print(y+1,row-x)
            break
        nx, ny = x+dx, y+dy
        if 0<= nx < row and 0<= ny < col and not lst[nx][ny]: # 같은방향 가능하다면
            x, y = nx, ny
        else:
            dir += 1
            dx, dy = dirx[dir%4], diry[dir%4]
            x, y = x+dx, y+dy
else:
    print(0)