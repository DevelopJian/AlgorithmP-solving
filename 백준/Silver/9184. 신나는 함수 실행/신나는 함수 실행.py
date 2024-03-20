# dp 테이블 만들기 (음수, 20초과 => 무조건 값이 같으므로 만들 필요없음.)
dp = [[[0]*21 for _ in range(21)] for _ in range(21)]
for i in range(21):
    for j in range(21):
        for k in range(21):
            if i == 0 or j == 0 or k == 0:
                dp[i][j][k] = 1
for i in range(1, 21):
    for j in range(1, 21):
        for k in range(1, 21):
            if i < j < k:
                dp[i][j][k] = dp[i][j][k-1] + dp[i][j-1][k-1] - dp[i][j-1][k]
            else:
                dp[i][j][k] = dp[i-1][j][k] + dp[i-1][j-1][k] + dp[i-1][j][k-1] - dp[i-1][j-1][k-1]
num = dp[20][20][20]

def w(i, j, k):
    if i<=0 or j<=0 or k<=0:
        return 1
    if i>20 or j>20 or k>20:
        return num
    else:
        return dp[i][j][k]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    print(f'w({a}, {b}, {c}) = {w(a, b, c)}')