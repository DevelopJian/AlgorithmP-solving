n = int(input())

lst = [[0]*100 for _ in range(100)]

for i in range(n):
    x, y = map(int, input().split())
    # 1표시하기
    for j in range(x, x+10):
        for k in range(y, y+10):
            lst[j][k] = 1
result = 0
for l in lst:
    result += sum(l)

print(result)