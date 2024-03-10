def dfs(cnt, lst):
    if cnt == m:
        print(*lst)
        return
    for i in range(n):
        dfs(cnt + 1, lst + [arr[i]])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs(0, [])