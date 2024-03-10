# 1~n일 동안 일한다
def dfs(sdate, sm):  # 일 시작 가능한 날, 지금까지 번 돈
    global mx
    if sdate >= n:
        mx = max(sm, mx)
        return
    for date in range(sdate, n):
        # 일 끝나는 날이 n보다 작을 때
        if date + tlst[date] - 1 < n:
            # v 표시 (시작날 ~ 끝나는 날)
            for i in range(date, date + tlst[date]):
                v[i] = 1
                dfs(date + tlst[date], sm + plst[date])
                v[i] = 0
        # 일 끝나는 날이 n보다 크다면 불가
        # -> 여기서 return 하면 안됨. for문이 다 안돌아가서 그 뒤의 경우의 수가 빠짐.
        else:
            dfs(n, sm)

n = int(input())
tlst = []
plst = []
for _ in range(n):
    a, b = map(int, input().split())
    tlst.append(a)
    plst.append(b)

v = [0] * n
mx = 0
dfs(0, 0)

print(mx)