from collections import deque

cursorL = deque(input())
cursorR = deque()

for _ in range(int(input())):
    order = input()
    if order == 'L' and cursorL:
        cursorR.append(cursorL.pop())
    elif order == 'D' and cursorR:
        cursorL.append(cursorR.pop())
    elif order == 'B' and cursorL:
        cursorL.pop()
    elif order[0] == 'P':
        cursorL.append(order[2:])

print(*cursorL, sep='', end ='')  # 정순으로 출력
while cursorR:  # 역순으로 출력
    print(cursorR.pop(), end ='')
