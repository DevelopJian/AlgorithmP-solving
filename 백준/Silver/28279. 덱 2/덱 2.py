from collections import deque
import sys
input = sys.stdin.readline

n = int(input().strip())
deq = deque()

for _ in range(n):
    order = input().strip()
    if len(order)>=3 and order[0] == '1':
        deq.appendleft(order[2:])
    elif len(order) >= 3 and order[0] == '2':
        deq.append(order[2:])
    elif order == '3':
        print(deq.popleft()) if deq else print(-1)
    elif order == '4':
        print(deq.pop()) if deq else print(-1)
    elif order == '5':
        print(len(deq))
    elif order == '6':
        print(0 if deq else 1)
    elif order == '7':
        print(deq[0]) if deq else print(-1)
    elif order == '8':
        print(deq[-1]) if deq else print(-1)