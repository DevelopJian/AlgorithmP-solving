def dfs(cnt, lst):
    if cnt == m:
        print(*lst)
        return

    prev = 0
    for i in range(n):
        if not v[i] and prev != arr[i]:
            prev = arr[i]
            v[i] = 1
            dfs(cnt + 1, lst + [arr[i]])
            v[i] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0] * n
dfs(0, [])