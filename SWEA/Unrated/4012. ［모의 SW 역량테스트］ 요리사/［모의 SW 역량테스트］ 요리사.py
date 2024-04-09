def dfs(idx, sma, lsta, smb, lstb): # 이번넣는다만다 인덱스, 뽑은것 계산, 뽑은것리스트(인덱스 들어있음), 안뽑은것 계산, 안뽑은것리스트
    global mn
    # 가지치기
    if len(lsta) > n//2 or len(lstb) > n//2:
        return
    # 종료조건
    if idx == n:
        # 정답처리
        if len(lsta) == n//2:
            mn = min(mn, abs(sma - smb))
        return
    # 하부함수
    #1. 뽑는다
    sm = 0 # 이번것과 지금까지 있던것의 시너지 합
    for i in lsta:
        sm += (arr[idx][i] + arr[i][idx])
    dfs(idx+1, sma+sm, lsta+[idx], smb, lstb)
    #2. 안뽑는다
    sm = 0
    for i in lstb:
        sm += (arr[idx][i] + arr[i][idx])
    dfs(idx+1, sma, lsta, smb+sm, lstb+[idx])
 
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
 
    mn = 10**9
    dfs(0, 0, [], 0, [])
 
    print(f'#{tc} {mn}')