def dfs(idx, sm):
    global ans
    if idx == n:
        if sm == k:
            ans += 1
        return
    dfs(idx + 1, sm + arr[idx])
    dfs(idx + 1, sm)

t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    v = [0] * n
    ans = 0
    dfs(0,0)

    print(f'#{tc} {ans}')