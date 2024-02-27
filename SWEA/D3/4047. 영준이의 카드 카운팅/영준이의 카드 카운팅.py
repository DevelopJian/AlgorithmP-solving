t = int(input())
for tc in range(1, t+1):
    string = input()
    n = len(string)
    s, d, h, c = [0] * 14, [0] * 14, [0] * 14, [0] * 14
    bools = True
    for i in range(0, n, 3):
        num = int(string[i+1:i+3])
        if string[i] == 'S':
            if s[num]:
                bools = False
                break
            else: s[num] = 1
        elif string[i] == 'D':
            if d[num]:
                bools = False
                break
            else: d[num] = 1
        elif string[i] == 'H':
            if h[num]:
                bools = False
                break
            else: h[num] = 1
        elif string[i] == 'C':
            if c[num]:
                bools = False
                break
            else: c[num] = 1
    if bools:
        print(f'#{tc} {13-sum(s)} {13-sum(d)} {13-sum(h)} {13-sum(c)}')
    else :
        print(f'#{tc} ERROR')
