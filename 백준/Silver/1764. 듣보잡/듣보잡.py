import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 여러줄 인풋받아서 바로 넣는 법(strip으로 개행문자 \n 없앰)
nohear = set(input().strip() for i in range(n))
nosee = set(input().strip() for i in range(m))

result = list(nohear&nosee)

print(len(result))
print(*sorted(result), sep = '\n')

# 리스트 겹치는 부분 구해라 -> 합집합!!!!
