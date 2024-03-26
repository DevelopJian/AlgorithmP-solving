import sys
input = sys.stdin.readline

t = int(input())
stack = []

for i in range(t):
    order = input().strip()

    if len(order) > 2 :
        stack.append(int(order[2:]))
    elif order == '2' :
        if len(stack) > 0:
            result = stack.pop(-1)
            print(result)
        else :
            print(-1)
    elif order == '3' :
        print(len(stack))
    elif order == '4' :
        if len(stack)== 0:
            print(1)
        else :
            print(0)
    elif order == '5' :
        if len(stack) > 0:
            print(stack[-1])
        else :
            print(-1)