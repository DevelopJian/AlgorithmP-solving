a, b = map(int, input().split())
x, y = map(int, input().split())
m, n = (a*y + b*x) , b*y

while n > 0:
  m, n = n, m%n
gcd = m

print( (a*y + b*x)//m , b*y //m )