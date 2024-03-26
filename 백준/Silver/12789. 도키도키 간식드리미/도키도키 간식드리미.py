import sys
input = sys.stdin.readline

n = int(input()) # 학생수
lst =list(map(int, input().split()))
stack = []

number = 1  # 찾는숫자

for i in range(n):
    stack.append(lst[i])
    while stack[-1] == number :
        stack.pop()
        number += 1
        if not stack :
            break

print('Sad' if stack else 'Nice')