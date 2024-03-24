t = int(input())
for tc in range(t):
    n = int(input())
    dct = {}
    types = set()
    for _ in range(n):
        name, type = input().split()
        if type not in dct:
            dct[type] = [name]
        else:
            dct[type].append(name)
        types.add(type)
    types = list(types)
    nums = []
    for tp in types:
        nums.append(len(dct[tp]))

    ans = 1
    for num in nums:
        ans *= (num + 1)

    print(ans-1)