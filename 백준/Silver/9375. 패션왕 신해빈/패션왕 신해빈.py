t = int(input())
for tc in range(t):
    n = int(input())
    types = {}
    typelst = []
    for _ in range(n):
        name, type = input().split()
        if type not in types:
            types[type] = 1
            typelst.append(type)
        else:
            types[type] += 1

    ans = 1
    for tp in typelst:
        ans *= (types[tp] + 1)

    print(ans-1)