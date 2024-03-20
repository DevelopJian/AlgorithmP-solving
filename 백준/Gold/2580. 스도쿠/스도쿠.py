import sys
input = sys.stdin.readline

def possible(x, y, num):
    # 가로검증
    for i in sudoku[x]:
        if i == num:
            return False
    # 세로검증
    for i in range(9):
        if num == sudoku[i][y]:
            return False
    # 박스검증
    r, c = x - (x % 3), y - (y % 3)
    for i in range(r, r+3):
        for j in range(c, c+3):
            if sudoku[i][j] == num:
                return False
    return True

def dfs(idx):
    global flag
    if flag:
        return
    if idx == n:
        for r in sudoku:
            print(*r)
            flag = True
        return
    for num in range(1, 10):
        x, y = lst[idx][0], lst[idx][1]
        if possible(x, y, num) == True:
            sudoku[x][y] = num
            dfs(idx + 1)
            sudoku[x][y] = 0

sudoku = [list(map(int, input().split())) for _ in range(9)]
lst = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j] == 0:
            lst.append((i, j))
n = len(lst)
flag = False
dfs(0)