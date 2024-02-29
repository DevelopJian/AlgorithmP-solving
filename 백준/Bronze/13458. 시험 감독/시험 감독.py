n = int(input()) # 시험장수
lst = list(map(int, input().split())) # 시험장마다 있는 응시자수
b, c = map(int, input().split()) # 총감 감시 가능수, 부감 감시 가능수

cnt = len(lst) # 총감독 한명씩 넣어줌
for num in lst:
    if num - b > 0 :
        if (num-b) % c == 0:
            cnt += (num-b)//c
        else:
            cnt += ((num-b)//c+1)
print(cnt)