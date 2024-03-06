def dfs(cnt, lst): # 고른 갯수, 고른 리스트
    # 종료조건
    if cnt == m:
        print(*lst)
        return

    for i in range(1, n+1):
        if not v[i]:
            v[i] = 1
            dfs(cnt+1, lst + [i])
            v[i] = 0

n, m = map(int, input().split())
v = [0] * (n+1)
dfs(0, [])