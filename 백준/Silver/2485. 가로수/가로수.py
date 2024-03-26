import sys
input = sys.stdin.readline

n = int(input()) # 심겨있는 가로수 수
subtract_lst = [] # 차 리스트 (갯수 n-1 개)
num = int(input())
for _ in range(n-1):
  a = int(input())
  subtract_lst.append(a-num)
  num = a
# 최대공약수 구하기
def gcd(a, b):  # a가 큰수
  while b>0:
    a, b = b, a%b
  return a
# 연쇄적으로 최대공약수 계산
y = subtract_lst[0]
for x in subtract_lst[1:] :
  y = gcd(x, y)
# 최대공약수 = y

# 리스트 안 숫자 // 최대공약수 -1 을 모두 더하기
result = 0
for i in subtract_lst:
  result += (i // y -1)

print(result)