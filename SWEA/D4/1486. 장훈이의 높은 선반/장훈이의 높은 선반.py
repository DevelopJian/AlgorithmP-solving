def dfs(num, sm): # 몇번째점원 0~(n-1), 키 합
    global mn_h
    if sm >= mn_h: # 가지치기(백트래킹)
        return
    if num == n:
        if sm >= b:
            mn_h = min(sm, mn_h)
        return
    dfs(num+1, sm + height[num]) # 이 점원 쌓였을 때
    dfs(num+1, sm) # 이 점원 안쌓였을 떄

t = int(input())
for tc in range(1, t+1):
    n, b = map(int, input().split())
    height = list(map(int, input().split()))
    mn_h = 200001

    dfs(0, 0)

    print(f'#{tc} {mn_h - b}')