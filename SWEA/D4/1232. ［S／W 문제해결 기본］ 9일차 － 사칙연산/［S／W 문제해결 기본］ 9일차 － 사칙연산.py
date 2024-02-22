from collections import deque
 
def post(now):
    if now : # now가 0이 아니면
        # 좌
        post(int(nodes[now][1]))
        # 우
        post(int(nodes[now][2]))
        # 현재노드
        deq.append(nodes[now][0])
def calculate(deq):
    stack = []
    while deq:
        num = deq.popleft()
        if num.isdigit():
            stack.append(int(num))
        else :
            b = stack.pop()  # 순서주의
            a = stack.pop()
            if num == '+':
                stack.append(a+b)
            elif num == '-':
                stack.append(a-b)
            elif num == '*':
                stack.append(a*b)
            else:
                stack.append(a//b)
    return stack

T = 10
for test_case in range(1, T + 1):
    n = int(input()) # 정점갯수
    nodes = [[0, 0, 0] for _ in range (n+1)] # 연결리스트(내값, 좌인덱스, 우인덱스) 만들기
    # 인덱스가 노드번호, 값이 노드값
    for i in range(n):
        lst = list(input().split())
        if lst[1].isdigit():
            nodes[int(lst[0])][0] = lst[1]
        else :
            nodes[int(lst[0])][0] = lst[1]
            nodes[int(lst[0])][1] = lst[2]
            nodes[int(lst[0])][2] = lst[3]
 
    deq = deque()
    post(1)
    print(f'#{test_case} {calculate(deq)[0]}')