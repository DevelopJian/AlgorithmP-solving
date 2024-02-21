def inOrder(now):
    if now != 0:  # 루트까지 올라간 후 종료
        if len(nodes[now]) > 2:  # 좌자식 있으면
            inOrder(int(nodes[now][2]))
        result.append(nodes[now][1])  # 현재노드
        if len(nodes[now]) > 3:  # 우자식 있으면
            inOrder(int(nodes[now][3]))
 
for test_case in range(1, 11):
    n = int(input()) # 노드수
    # 연결리스트 [ 현재인덱스, 현재값, 좌인덱스, 우인덱스 ]
    nodes = [input().strip().split() for _ in range(n)]
    nodes = [[]] + nodes  # 안쓰는 0번 추가
    result = []
    inOrder(1)  # 루트부터 시작
 
    print(f'#{test_case}', end =' ')
    print(*result, sep='')