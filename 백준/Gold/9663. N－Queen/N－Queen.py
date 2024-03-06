def dfs(i):  # i = 위치 고를 row
    global ans
    # 종료조건
    if i == n:
        ans += 1
        return
    
    for j in range(n): # row = i 에서 col j를 고름
        if not v1[j] and not v2[i-j] and not v3[i+j]:
            v1[j], v2[i-j], v3[i+j] = 1, 1, 1
            dfs(i + 1)
            v1[j], v2[i-j], v3[i+j] = 0, 0, 0

n = int(input())
v1 = [0] * n # col
v2 = [0] * 40 # \ 대각선 (뺀것이 같음)
v3 = [0] * 40 # / 대각선 (더한것이 같음)
ans = 0
# 시작점 고르기(row = 0 에서 시작)
for col in range(n):
    v1[col], v2[0-col], v3[0+col] = 1, 1, 1
    dfs(1)
    v1[col], v2[0-col], v3[0+col] = 0, 0, 0

print(ans)