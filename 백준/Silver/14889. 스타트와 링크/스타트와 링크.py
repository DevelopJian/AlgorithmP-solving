def dfs(p, alst, blst):
    global mn
    # 가지치기
    if len(alst) > n//2 or len(blst) > n//2:
        return
    # 종료조건
    if p == n:
        if len(alst) == len(blst):
            asum, bsum = 0, 0
            for i in range(n // 2):
                for j in range(n // 2):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            mn = min(mn, abs(asum - bsum))
        return
    # 하부함수
    dfs(p+1, alst + [p], blst)
    dfs(p+1, alst, blst + [p])

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
mn = 100000
dfs(0, [], [])
print(mn)