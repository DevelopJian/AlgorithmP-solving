from collections import deque

string = input()
cursorL = deque()
cursorR = deque()

# 초기에 커서가 제일 우측에 있으니 cursorL에 순서대로 모두 넣고 시작
for ch in string:
    cursorL.append(ch)

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