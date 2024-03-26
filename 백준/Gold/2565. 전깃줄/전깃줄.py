import sys
input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    a, b = map(int, input().split())
    arr.append((a, b))
arr.sort()

dp = [1] * n
for i in range(1, n):
    for j in range(i):
        if arr[i][1] > arr[j][1] and dp[i] < dp[j] + 1:
            dp[i] = dp[j] + 1
ans = n - max(dp)
print(ans)