def dfs(cnt, lst): # 고른 숫자 갯수, 고른 숫자 리스트
    if cnt == m:
        print(*lst)
        return
    for num in range(1, n+1):
        dfs(cnt + 1, lst + [num])

n, m = map(int, input().split())
dfs(0, [])