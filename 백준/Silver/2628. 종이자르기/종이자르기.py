a, b = map(int, input().split()) # 가로세로
n = int(input())
alst = [0] # 가로리스트
alst.append(a)
blst= [0] # 세로리스트
blst.append(b)

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        blst.append(b)
    else:
        alst.append(b)
alst.sort()
blst.sort()
# 차이들 리스트만들기
xlst = []
ylst = []
for i in range(len(alst)-1):
    xlst.append(alst[i+1]-alst[i])
for i in range(len(blst)-1):
    ylst.append(blst[i+1]-blst[i])
mx = 0
for x in xlst:
    for y in ylst:
        mx = max(mx, x*y)

print(mx)