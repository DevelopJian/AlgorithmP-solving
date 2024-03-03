for _ in range(10):
    tc = int(input())
    arr = [list(input()) for _ in range(100)]
    mx = 1
    # 가로확인
    for l in range(2, 101): # l = 문자길이
        for i in range(100):
            for j in range(l, 101): # j 는 끝인덱스
                if arr[i][j-l:j] == arr[i][j-1 : j-l-1 : -1]:
                    mx = max(mx, l)
    # 세로확인
    arr2 = list(zip(*arr))
    for l in range(2, 101): # l = 문자길이
        for i in range(100):
            for j in range(l, 101): # j 는 끝인덱스
                if arr2[i][j-l:j] == arr2[i][j-1 : j-l-1 : -1]:
                    mx = max(mx, l)

    print(f'#{tc} {mx}')