l = int(input())
cake = [0]*(l+1)
n = int(input())
mxnum, mx = 0, 0 # 최대 기대한 사람, 최대 기대한 조각
mxp, mxcnt = 0, 0 # 실제 최대 많이 가져간 사람, 최대 가져간 조각 수
for num in range(1,n+1):
    s, e = map(int, input().split())
    if mx < e-s+1:
        mx, mxnum = e-s+1, num
    cnt = 0 # 가져간 케이크 수
    for i in range(s, e+1):
        if not cake[i]:
            cake[i] = num
            cnt += 1
    if cnt > mxcnt :
        mxp, mxcnt = num, cnt

print(mxnum, mxp, sep = '\n')
