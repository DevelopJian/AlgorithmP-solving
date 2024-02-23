lst = list(int(input()) for _ in range(9))
sm = sum(lst)
result = False
for i in range(8):
    for j in range(i+1, 9):
        if sm-lst[i]-lst[j] == 100:
            lst.pop(j)
            lst.pop(i)
            result = True
            break
    if result :
        break

lst.sort()
for i in lst:
    print(i)