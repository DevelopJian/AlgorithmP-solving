def check(): # 가로세로 체크
    for i in range(n):
        for j in range(n):
            for dx, dy in ((0,1),(1,0),(1,1),(1,-1)): #가로 세로 \ /
                nx, ny = i, j
                cnt = 0
                while 0<= nx <n and 0<= ny <n :
                    if board[nx][ny] == 'o':
                        cnt += 1
                    else:
                        cnt = 0
                    if cnt == 5:
                        return True
                    nx, ny = nx+dx, ny+dy
    return False

t = int(input())
for tc in range(1, t+1):
    n = int(input())
    board = [list(input()) for _ in range(n)]
    if check():
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')