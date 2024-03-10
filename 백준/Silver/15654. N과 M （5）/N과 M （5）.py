def dfs(cnt, lst):  # 고른 갯수, 고른 수 리스트
    if cnt == m:
        print(*lst)
        return
    for idx in range(n):
        if not v[idx]:
            v[idx] = 1
            dfs(cnt + 1, lst + [arr[idx]])
            v[idx] = 0

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
v = [0] * n

dfs(0, [])