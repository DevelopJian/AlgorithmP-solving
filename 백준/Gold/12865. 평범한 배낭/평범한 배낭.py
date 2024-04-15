n, k = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(n)]
dp = [[0] + [-1] * k for _ in range(n)]
if lst[0][0] <= k:
    dp[0][lst[0][0]] = lst[0][1]

for row in range(1, n):
    for col in range(k+1):
        if dp[row-1][col] != -1:
            if col+lst[row][0] <= k and dp[row][col+lst[row][0]] < dp[row-1][col] + lst[row][1]: # 무게가 넘어가지 않는다면
                dp[row][col+lst[row][0]] = dp[row-1][col] + lst[row][1]
            if dp[row][col] <= dp[row-1][col]:
                dp[row][col] = dp[row-1][col]
ans = 0
for l in dp:
    if max(l) > ans:
        ans = max(l)

print(ans)
