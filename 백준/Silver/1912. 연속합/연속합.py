n = int(input())
arr = list(map(int, input().split()))

mx = -1000
dp = 0

for i in range(n):
    if arr[i] <= arr[i] + dp:
        dp += arr[i]
    else:
        dp = arr[i]
    mx = max(mx, dp)

print(mx)