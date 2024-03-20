def fun(n):
    dp = [0] * 1000001
    dp[1], dp[2] = 1, 2
    if n > 2:
        for i in range(3, n+1):
            dp[i] = (dp[i-1] + dp[i-2]) % 15746
    return dp[n]

n = int(input())
print(fun(n))