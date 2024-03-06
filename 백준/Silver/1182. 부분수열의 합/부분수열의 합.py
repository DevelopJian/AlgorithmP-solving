def dfs(idx, sm, cnt):
    global ans
    if idx == n:
        if sm == s and cnt > 0:
            ans += 1
        return
    dfs(idx + 1, sm + arr[idx], cnt + 1)
    dfs(idx + 1, sm, cnt)

n, s = map(int, input().split())
arr = list(map(int, input().split()))
ans = 0
dfs(0, 0, 0)

print(ans)