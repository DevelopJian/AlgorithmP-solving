n = int(input())
stack = []
want = [int(input()) for _ in range(n)]
result = []

now = 1
for i in want :
    while now <= n+1 :  # 같거나?
        if not stack:
            stack.append(now)
            now += 1
            result.append('+')
        elif stack and stack[-1]!= i :
            stack.append(now)
            now += 1
            result.append('+')
        elif stack and stack[-1] == i :
            stack.pop()
            result.append('-')
            break

    if  now > n+1 :
        result = 'NO'
        break

print('\n'.join(result) if result != 'NO' else result)