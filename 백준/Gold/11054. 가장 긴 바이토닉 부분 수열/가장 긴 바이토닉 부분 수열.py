import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

dp = [[1]*n for _ in range(3)]

# 올라가는 수열 dp[0]
for i in range(1, n):
    for j in range(i):
        if arr[i] > arr[j] and dp[0][i] < dp[0][j] + 1:
            dp[0][i] = dp[0][j] + 1

# 내려가는 수열 dp[1]
for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if arr[i] > arr[j] and dp[1][i] < dp[1][j] + 1:
            dp[1][i] = dp[1][j] + 1

# 합 dp[2]
for i in range(n):
    dp[2][i] = dp[0][i] + dp[1][i]

# 답 = 합의 max -1
ans = max(dp[2]) - 1
print(ans)