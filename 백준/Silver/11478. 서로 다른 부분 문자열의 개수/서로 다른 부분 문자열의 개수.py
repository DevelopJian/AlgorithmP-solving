s = input()
n = len(s)
resultset = set() # 중북방지 # set만들때 주의!!! dict랑 다름

for i in range(n): # start : 0~(n-1)
    for j in range(i, n): # finish : i~ (n-1)
        resultset.add(s[i:j+1])

print(len(resultset))