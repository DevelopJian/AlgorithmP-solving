import sys
input = sys.stdin.readline
# n이 루트n 보다 작은 약수를 가지지 않으면 소수다!!
def isprime(x):
  for i in range(2, int(x**0.5)+1):
    if x % i == 0:
      return False
  return True

t = int(input())
for tc in range(t):
  n = int(input())

  while True :
    if n == 0 or n ==1 :
      print(2)
      break
    elif isprime(n):
      print(n)
      break
    else:
      n += 1