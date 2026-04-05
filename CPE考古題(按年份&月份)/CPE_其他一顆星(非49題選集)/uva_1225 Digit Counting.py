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
