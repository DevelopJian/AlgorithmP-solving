for tc in range(1, 11):
    input() 
    table = [list(map(int, input().split())) for _ in range(100)]  # 1=n극 2=s극  // 위에 n극  아래에 s극
    # 위1 아래2 붙어있는 나오는 갯수 구하기 -> 열마다
    cnt = 0
    for i in range(100):
        flag = 0
        for j in range(100):
            if table[j][i] == 1:
                flag += 1
            elif table[j][i] == 2: # 위에서 n극이 하나라도 나왔는데 s극 나오면
                if flag:
                    cnt += 1
                    flag = 0
 
    print(f'#{tc} {cnt}')