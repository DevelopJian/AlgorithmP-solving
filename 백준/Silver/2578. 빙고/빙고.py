import sys
input = sys.stdin.readline

bingo = [list(map(int, input().split())) for _ in range(5)]
lst = [0] # 안쓰는 0번째 채워줌
temp = [[0]*5 for _ in range(5)]
for i in range(5):
    lst = lst + list(map(int, input().split()))

for num in range(1, 26): # num = 사회자가 부르는 수 몇번째인지
    flag = False
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == lst[num]:
                temp[i][j] = num
                flag = True
                break
        if flag:
            break

# temp 줄마다 가장 큰 수 뽑기 -> 그 중 3번째로 작은수
temp2 = list(zip(*temp)) # 전치행렬
anslst =[]
for i in range(5):
    anslst.append(max(temp[i])) # 가로
    anslst.append(max(temp2[i])) # 세로
mxa, mxb = 0, 0 # \ /
for i in range(5):
    mxa = max(mxa, temp[i][i])
    mxb = max(mxb, temp[i][4-i])
anslst.append(mxa)
anslst.append(mxb)

print(sorted(anslst)[2])