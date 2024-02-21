t = int(input())
for test_case in range(1, 1+t):
    n = int(input())
    result = -1
 
    start = 1
    end = n//2 + 2 # 경우의 수 줄여주기
    while start <= end :
        mid = (start + end) // 2
        if mid**3 == n:
            result = mid
            break
        elif mid**3 > n:
            end = mid - 1
        elif mid**3 < n:
            start = mid + 1
    print(f'#{test_case} {result}')