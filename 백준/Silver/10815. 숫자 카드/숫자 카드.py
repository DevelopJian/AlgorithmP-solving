n = int(input())
intset = set(map(int, input().split()))
m = int(input())
lst = list(map(int, input().split()))

for i in lst :
    if i in intset:
        print(1, end = ' ')
    else :
        print(0, end = ' ')