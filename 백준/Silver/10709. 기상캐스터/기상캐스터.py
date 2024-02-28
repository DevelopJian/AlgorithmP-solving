h, w = map(int, input().split()) # 세로길이, 가로길이
sky = [list(input()) for _ in range(h)]
ans = [[-1] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if sky[i][j] == 'c':
            ans[i][j] = 0
            dst = 1
            for col in range(j+1, w):
                ans[i][col] = dst
                dst += 1
for l in ans:
    print(*l)