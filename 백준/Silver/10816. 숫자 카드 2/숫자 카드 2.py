n = int(input()) # 숫자카드 갯수 500,000
lst = list(map(int, input().split()))
m = int(input())  # m을 몇개갖고있냐(500,000)
finding = list(map(int, input().split()))  # 여러번 찾아야함(500,000) -> 시간복잡도때문에 갯수 딕셔너리 만들어서 바로 찾는게 좋음
numdict ={}

for num in lst :
    if num in numdict :
        numdict[num] += 1
    else :
        numdict[num] = 1

for i in finding :
    if i not in numdict :
        print(0, end = ' ')
    else :
        print(numdict[i], end = ' ')