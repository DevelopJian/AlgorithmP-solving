n = int(input())
dp = [0] * (n+1) # 인덱스가 수, 값이 몇번째 연산인지
dp[n] = 1

for i in range(n, 0, -1):
    if dp[i]:
        if i % 3 == 0 and (dp[i//3] > dp[i] + 1 or dp[i//3] == 0):
            dp[i//3] = dp[i] + 1
        if i % 2 == 0 and (dp[i//2] > dp[i] + 1 or dp[i//2] == 0):
            dp[i//2] = dp[i] + 1
        if dp[i-1] > dp[i] + 1 or dp[i-1] == 0:
            dp[i-1] = dp[i] + 1

print(dp[1] - 1)