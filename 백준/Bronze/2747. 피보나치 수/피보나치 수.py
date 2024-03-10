n = int(input())
fibo = [0] * (n+1)
fibo[1] = 1

x = 2
while x <= n:
    fibo[x] = fibo[x-2] + fibo[x-1]
    x += 1

print(fibo[n])