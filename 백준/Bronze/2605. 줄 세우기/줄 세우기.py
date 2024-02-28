# 뽑은 번호만큼 앞으로가서 줄선다
# 학생 1번부터 시작

n = int(input())
stu = list(range(n+1))
lst = [0] + list(map(int, input().split()))

for i in range(2, n+1):
    stu.insert(i-lst[i],stu[i])
    stu.pop(i+1)

print(*stu[1:])