# 이진트리
def dfs(num, lst):
    if num == n+1:
        if len(lst) == m:
            print(*lst)
        return
    dfs(num + 1, lst + [num])
    dfs(num + 1, lst)

n, m = map(int, input().split())
dfs(1, [])