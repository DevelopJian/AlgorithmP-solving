def dfs(el, sm): # 원소갯수, 지금까지합
    global cnt
    if sm > n: # 가지치기
        return
    # 종료조건 2개 : 원소수 초과, 합에 도달
    if el == n+1 :
        return
    if sm == n:
        cnt += 1
    for i in lst:
        dfs(el+1, sm+i)

t = int(input())
for tc in range(t):
    n = int(input())
    cnt = 0
    lst = [1, 2, 3]
    dfs(0, 0)

    print(cnt)