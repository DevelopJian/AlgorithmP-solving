from collections import deque
import sys
input = sys.stdin.readline

que = deque() # deque object
n = int(input())

for _ in range(n):
    order = input().strip()

    if len(order)>= 6:  # push X
        que.append(int(order[5:]))
    elif order == 'pop':
        if not que :
            print(-1)
        else :
            result = que.popleft()
            print(result)
    elif order == 'size':
        print(len(que))
    elif order == 'empty':
        if que :
            print(0)
        else :
            print(1)
    elif order == 'front':
        if que :
            print(que[0])
        else :
            print(-1)
    elif order == 'back':
        if que :
            print(que[-1])
        else :
            print(-1)