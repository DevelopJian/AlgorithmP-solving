import sys
input = sys.stdin.readline

arr1 = [0] + list(input().strip())
arr2 = [0] + list(input().strip())
n, m = len(arr1), len(arr2)

dp = [[0] * m for _ in range(n)]
for i in range(1, n):
    for j in range(1, m):
        if arr1[i] == arr2[j]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[n-1][m-1])
