
t = int(input())
for i in range(t):
    string = input()
    bools = True
    stack = []

    for ho in string :
        if ho == '(':
            stack.append(ho)
        else :  # )
            if len(stack) == 0:
                bools = False
                break
            else :
                if stack[-1] == ')':
                    bools = False
                    break
                else :
                    stack.pop(-1)
    if bools == True :
        if len(stack) > 0:
            print('NO')
        else :
            print('YES')
    else:
        print('NO')

