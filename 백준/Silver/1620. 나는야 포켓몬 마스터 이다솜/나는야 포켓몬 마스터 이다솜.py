n, m = map(int, input().split())

dogam = {} # key = 숫자 , value = 이름
dogam2 = {} # value = 이름, key = 숫자
for i in range(1, n+1):
    a = input()
    dogam[i] = a
    dogam2[a] = i
for _ in range(m):
    exam = input()
    if exam.isalpha() :
        print(dogam2[exam])
    else :
        print(dogam[int(exam)])