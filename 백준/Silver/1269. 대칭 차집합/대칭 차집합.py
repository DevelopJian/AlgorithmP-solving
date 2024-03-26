a, b = map(int, input().split())
seta = set(map(int, input().split()))
setb = set(map(int, input().split()))
print(len((seta|setb)-(seta&setb)))