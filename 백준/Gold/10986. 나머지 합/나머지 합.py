n, m = map(int, input().split()) # 수 n개, 합이 m으로 나누어떨어지는
numbers = list(map(int, input().split())) #맨앞 0포함 숫자

sumnumbers = [0]*n # 구간합(맨앞 0 추가)
sums = 0
for i in range(n):
    sums += numbers[i]
    sumnumbers[i] = sums
dvnumbers = [0]*n

for i in range(n):  # 나머지 리스트 만들어줌(맨앞 0 추가)
    dvnumbers[i] = sumnumbers[i] % m

# 서로 뺐을 떄 0인 조합 찾기(같은 수의 2개씩 combination 찾기)
cnt = dvnumbers.count(0)
for i in range(0, m):
    a = dvnumbers.count(i)
    cnt += a * (a-1) // 2

print(cnt)