import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dp[0][0] = arr[0][0]

for i in range(1, n):
    for j in range(i+1):
        if j > 0: # 범위 안 (위쪽 j, j-1 중에 고르기)
            dp[i][j] = arr[i][j] + max(dp[i-1][j-1], dp[i-1][j])
        else: # 범위 벗어나면 (위쪽 j를 고르기)
            dp[i][j] = arr[i][j] + dp[i-1][j]
ans = max(dp[n-1])
print(ans)
