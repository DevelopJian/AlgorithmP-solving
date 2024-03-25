n = int(input())
dp = [[0]*10 for _ in range(n+1)]
# dp[자리수][끝수]

# 자리수 = 1
for end in range(1, 10):
    dp[1][end] = 1

for cnt in range(2, n+1):
    for end in range(0, 10):
        if end == 0:
            dp[cnt][end] = dp[cnt-1][end+1]
        elif end == 9:
            dp[cnt][end] = dp[cnt-1][end-1]
        else:
            dp[cnt][end] = dp[cnt-1][end-1] + dp[cnt-1][end+1]

print(sum(dp[n]) % 1000000000)