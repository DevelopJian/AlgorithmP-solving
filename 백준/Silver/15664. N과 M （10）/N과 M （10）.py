def dfs(cnt, start, lst):
    if cnt == m:
        print(*lst)
        return
    last = 0
    for i in range(start, n):
        if arr[i] != last:
            last = arr[i]
            dfs(cnt + 1, i + 1, lst + [arr[i]])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

dfs(0, 0,[])