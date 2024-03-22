import sys
input = sys.stdin.readline
inf = float('inf')

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*3 for _ in range(n)]
# 초기 값 할당
dp[0][0], dp[0][1], dp[0][2] = arr[0][0], arr[0][1], arr[0][2]

# arr의 값을 현재로 고정해두고, 윗줄의 dp 값 중 작은 것을 현재위치 dp에 할당
for i in range(1, n):
    for j in range(3):
        mn = inf
        for k in range(3): # 윗줄의 col
            if k == j:
                continue
            mn = min(mn, dp[i-1][k] + arr[i][j])
        dp[i][j] = mn

ans = min(dp[n-1])
print(ans)