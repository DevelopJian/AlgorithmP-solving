from collections import deque
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lst = deque(list(map(int, input().split())))
    stack = deque()

    earn = 0
    mx, sm = 0, 0 # 현재 젤 큰값, 그것보다 작은값들 합
    for i in range(len(lst)):
        num = lst.pop()
        if stack:
            if mx >= num:
                stack.append(num)
                sm += num
            else: # mx < num
                earn += mx * (len(stack)-1) - sm
                stack = deque([num]) 
                mx, sm = num, 0 # 초기화

        else:
            stack.append(num)
            mx = num
    if stack:
        earn += mx * (len(stack)-1) -sm

    print(f'#{tc} {earn}')
