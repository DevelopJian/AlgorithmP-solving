n = 4
arr = [[0]*8] + [list(map(int, input())) for _ in range(n)]
k = int(input())
top = [0] * (n+1)

for _ in range(k):
    idx, dr = map(int, input().split())
    # 톱니 회전
    tlst = [(idx, 0)]
    # 우측 처리
    for i in range(idx + 1, n+1):
        # 왼쪽 3시 != 우측 9시 => 회전
        if arr[i-1][(top[i-1]+2) %8] != arr[i][(top[i]+6)%8]:
            tlst.append((i, (i-idx)%2))
        else:
            break
    # 좌측 처리
    for i in range(idx - 1, 0, -1):
        # 왼쪽 3시 != 우측 9시 => 회전
        if arr[i][(top[i]+2) %8] != arr[i+1][(top[i+1]+6)%8]:
            tlst.append((i, (idx-i)%2))
        else:
            break
    # 회전
    for i, rot in tlst:
        if rot == 0:
            top[i] = (top[i]-dr+8)%8
        else:
            top[i] = (top[i]+dr+8) % 8
# 정답 계산
ans = 0
tbl = [0, 1, 2, 4, 8]
for i in range(1, n+1):
    ans += arr[i][top[i]] * tbl[i]
print(ans)