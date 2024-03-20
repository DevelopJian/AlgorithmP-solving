# 재귀
def fib(n):
    global ans1
    if n == 1 or n== 2:
        ans1 += 1
        return 1
    return fib(n-1) + fib(n-2)
# DP
def fibonacci(n):
    global ans2
    dp[1] = dp[2] = 1
    for i in range(3, n+1):
        dp[i] = dp[i-1] + dp[i-2]
        ans2 += 1
    return dp[n]

n = int(input())
ans1 = ans2 = 0
dp = [0] * (n+1)
fib(n)
fibonacci(n)

print(ans1, ans2)