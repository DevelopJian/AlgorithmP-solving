def dfs(cnt, start, lst):
    if cnt == m:
        print(*lst)
        return
    for num in range(start, n+1):
        dfs(cnt + 1, num, lst + [num])

n, m = map(int, input().split())

dfs(0, 1,[])