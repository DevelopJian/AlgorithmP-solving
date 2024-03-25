import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [1] * n

for now in range(1, n):
    for pre in range(now):
        if arr[pre] < arr[now]:
            dp[now] = max(dp[now], dp[pre]+1)

print(max(dp))