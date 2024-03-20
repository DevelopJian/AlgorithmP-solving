dp = [[[1]*21 for _ in range(21)] for _ in range(21)]
# dp 초기값 1로 만들어주는 이유는 어차피 하나라도 0이면 값이 1이기 때문에.
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