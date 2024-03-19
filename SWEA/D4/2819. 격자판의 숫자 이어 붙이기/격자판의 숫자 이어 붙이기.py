def dfs(cnt, num, ci, cj):
    if cnt == 7:
        nums.add(num)
        return
    for di, dj in ((-1, 0), (0, 1), (1, 0), (0, -1)):
        ni, nj = ci + di, cj + dj
        if 0 <= ni < 4 and 0 <= nj < 4:
            dfs(cnt + 1, num*10 + arr[ni][nj], ni, nj)

t = int(input())
for tc in range(1, t + 1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    nums = set()

    for i in range(4):
        for j in range(4):
            dfs(1, arr[i][j], i, j)

    print(f'#{tc} {len(nums)}')