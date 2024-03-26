import sys
input = sys.stdin.readline
n = int(input())

logdict = {}
for _ in range(n):
    name, log = input().split()
    if log == 'enter':
        logdict[name] = log      
    else :
        del logdict[name]
              
atd = sorted(list(logdict.keys()), reverse = True)
print(*atd, sep='\n')
