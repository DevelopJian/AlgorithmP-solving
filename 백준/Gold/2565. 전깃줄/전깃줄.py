import sys
input = sys.stdin.readline

n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
arr.sort()

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
ans = n - max(dp)
print(ans)