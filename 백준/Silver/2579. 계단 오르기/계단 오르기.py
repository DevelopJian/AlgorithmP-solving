n = int(input())  # 계단 갯수
arr = [int(input()) for _ in range(n)]
if n == 1:
    print(arr[0])
elif n == 2:
    print(arr[0] + arr[1])
else:
    dp = [0] * n
    # 초기값 설정
    dp[0] = arr[0]
    dp[1] = arr[0] + arr[1]
    dp[2] = max(arr[0] + arr[2], arr[1] + arr[2])
    # dp 채우기
    for st in range(3, n):
        dp[st] = max(arr[st]+dp[st-2], arr[st]+dp[st-3]+arr[st-1])

    print(dp[n-1])