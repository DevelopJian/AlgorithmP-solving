def dfs(cnt, start, lst): # 숫자 뽑은 갯수, 이번 시작점, 뽑은 리스트
    if cnt == m:
        print(*lst)
        return
    for i in range(start, n):
        dfs(cnt + 1, i, lst + [arr[i]])

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
dfs(0, 0,[])