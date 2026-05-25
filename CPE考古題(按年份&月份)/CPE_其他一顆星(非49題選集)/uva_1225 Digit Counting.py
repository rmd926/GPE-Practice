tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    temp = ""
    lookup = {"0": 0, "1": 0, "2": 0, "3": 0, "4": 0, "5": 0, "6": 0, "7": 0, "8": 0, "9": 0}

    for i in range(1, n+1):
        temp += str(i)
    
    for ch in temp:
        if ch not in lookup:
            lookup[ch] = 1
        else:
            lookup[ch] += 1
    
    ans = []
    for key, value in sorted(lookup.items()):
        ans.append(value)
    
    print(*ans)

# 2026.05.26 二刷 注意記得要把lookup先建好，因為會有那種出現次數為0的case，若沒建output會沒有
