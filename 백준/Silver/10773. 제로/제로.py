import sys
input = sys.stdin.readline

stack = []
k = int(input())
for tc in range(k):
    n = int(input())
    if n == 0:
        stack.pop(-1)
    else :
        stack.append(n)

print(sum(stack))