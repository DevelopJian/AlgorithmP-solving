ia, ib = map(int, input().split())
a = ia
b = ib
while b > 0:
  a, b = b, a % b

result = ia * ib // a
print(result)