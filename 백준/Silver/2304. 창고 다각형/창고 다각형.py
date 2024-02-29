n = int(input()) # 기둥수
lst = [0] * 1002 # 안쓰는 0인덱스
mxidx, mx = 0, 0
for _ in range(n):
    a, b = map(int, input().split())
    lst[a] = b
    if mx < b:
        mx, mxidx = b, a

lsta  = lst[:mxidx] # mx 전
lstb = lst[len(lst)-1:mxidx-1:-1] # mx + mx 후

last1 = 0
last2 = 0
sm = 0
for i in range(len(lsta)):
    if lsta[i] > last1:
        last1 = lsta[i]
    sm += last1
for i in range(len(lstb)):
    if lstb[i] > last2:
        last2 = lstb[i]
    sm += last2

print(sm)