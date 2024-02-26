for _ in range(10):
    tc = input()
    lst = [list(map(int, input().split())) for _ in range(100)]
    lst2 = list(zip(*lst)) # 전치행렬
    mx = 0

    # 행의 합, 열의 합 최댓값구하기
    sm, sm2 = 0, 0
    for i in range(100):
        mx = max(sum(lst[i]), sum(lst2[i]), mx)
        sm += lst[i][i]
        sm2 += lst[i][99-i]

    mx = max(mx, sm, sm2)

    print(f'#{tc} {mx}')
