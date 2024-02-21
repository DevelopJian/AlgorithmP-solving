def dfs(idx, sm, cnt): # 들어있는 원소갯수
    global result
    # 종료조건
    if idx == n:
        if sm == s and cnt > 0:
            result += 1
        return
    dfs(idx +1, sm +arr[idx], cnt+1) # 이번원소 넣는것
    dfs(idx +1, sm, cnt) # 이번원소 안넣는것

n, s = map(int, input().split())
arr = list(map(int, input().split()))
result = 0
dfs(0, 0, 0)

print(result)
