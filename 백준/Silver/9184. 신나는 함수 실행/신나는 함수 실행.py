dp = [[[0]*101 for _ in range(101)] for _ in range(101)]
for i in range(-50, 51):
    for j in range(-50, 51):
        for k in range(-50, 51):
            if i <= 0 or j <= 0 or k <= 0:
                dp[i][j][k] = 1
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
num = dp[20][20][20]
for i in range(1, 51):
    for j in range(1, 51):
        for k in range(1, 51):
            if i > 20 or j > 20 or k > 20:
                dp[i][j][k] = num

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {dp[a][b][c]}')