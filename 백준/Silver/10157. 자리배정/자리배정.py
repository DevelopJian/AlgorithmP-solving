import sys
input = sys.stdin.readline

col, row = map(int, input().split()) # 갯수
k = int(input())
lst = [[0]*col for _ in range(row)]

if col * row < k:
    print(0)
else:
    # dir = 상 우 하 좌 반복
    dirx = [-1, 0, 1, 0]
    diry = [0, 1, 0, -1]
    x, y, dir = row-1, 0, 0
    for num in range(1, k+1): # num = 적을 숫자
        if num == k:
            print(y+1, row-x)
            break
        lst[x][y] = num
        nx, ny = x+dirx[dir], y+diry[dir]
        if 0<= nx < row and 0<= ny < col and not lst[nx][ny]: # 같은방향 가능하다면
            x, y = nx, ny
        else:
            dir = (dir+1)%4
            x, y = x + dirx[dir], y + diry[dir]