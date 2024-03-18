def dfs(cnt, sm, total, ci, cj): # 꿀 합, 이익
    global mx
    # 가지치기
    if sm > c:
        return
    # 종료조건, 정답처리
    if cnt == m:
        mx = max(total, mx)
        return
    # 재귀 호출
    dfs(cnt+1, sm+arr[ci][cj+cnt], total+(arr[ci][cj+cnt])**2, ci, cj) # 넣은것
    dfs(cnt+1, sm, total, ci, cj)# 안넣은것

t = int(input())
for tc in range(1, t+1):
    n, m, c = map(int, input().split()) # 벌통크기, 인당 벌통 수, 인당 꿀 채취 최대양
    arr = [list(map(int, input().split())) for _ in range(n)]

    ans, sm1 = 0, 0
    for i1 in range(n):
        for j1 in range(n-m+1):
            mx = 0
            dfs(0, 0, 0, i1, j1)  # (i1, j1)에서의 일꾼 1의 최대값 구해주기
            sm1 = mx # 일꾼 1의 최댓값 저장
            for i2 in range(i1, n):
                sj = j1 + m if i1 == i2 else 0 # 같은 행인지 아닌지
                for j2 in range(sj, n-m+1):
                    mx = 0 # 앞에서 썼기 때문에 초기화
                    dfs(0, 0, 0, i2, j2)
                    ans = max(ans, sm1+mx)

    print(f'#{tc} {ans}')