# 하나하나 확인할 시 100_000 * 100_000 = 10_000_000_000 -> 약 500초 걸림
# 이진탐색 : nums를 sort() 하면 O(NlogN) + 이진탐색 O(logN)
# log100_000 = 대략 20보다 작음.  20*100_000 = 2_000_000  -> 가능!
# 로직 : nums를 sort -> finds 를 이진탐색으로 찾는다

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
m = int(input())
finds = list(map(int, input().split()))

# 이진탐색
for i in range(m) :  # i = finds 인덱스
    exist = False
    start, end = 0, n-1  # s, e, m = nums 인덱스
    while start <= end : # 종료조건!!
        mid = (start + end) // 2  # nums 중간의 인덱스
        if finds[i] > nums[mid]:
            start = mid + 1  # 인덱스 이동
        elif finds[i] < nums[mid]:
            end = mid - 1 # 인덱스 이동
        else : # 찾으면
            exist = True
            break
    if exist:
        print(1)
    else :
        print(0)