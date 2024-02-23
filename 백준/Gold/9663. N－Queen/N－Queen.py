def dfs(row):
    global cnt
    if row == n:
        cnt += 1
        return
    for col in range(n):
        if v1[col] == v2[col-row] == v3[col+row] == 0:
            v1[col] = v2[col-row] = v3[col+row] = 1
            dfs(row+1)
            v1[col] = v2[col-row] = v3[col+row] = 0

n = int(input())
cnt = 0
v1 = [0]*n # 세로
v2 = [0]*(n*2) # 대각선
v3 = [0]*(n*2) # 대각선
dfs(0)

print(cnt)