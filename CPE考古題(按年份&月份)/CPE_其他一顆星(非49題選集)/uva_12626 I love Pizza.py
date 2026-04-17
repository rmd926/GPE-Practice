tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break
    
    component = "MARGARITA"
    for ch in target:
        if ch not in component:
            target = target.replace(ch, "")
    
    lookup = {}
    need = {"M":1, "A":3, "R":2, "G":1, "I":1, "T":1}

    for ch in target:
        if ch not in lookup:
            lookup[ch] = 1
        else:
            lookup[ch] += 1

    ans = float('inf')
    for key, value in need.items():
        ans = min(ans, lookup.get(key, 0) // value)
    
    print(ans)
