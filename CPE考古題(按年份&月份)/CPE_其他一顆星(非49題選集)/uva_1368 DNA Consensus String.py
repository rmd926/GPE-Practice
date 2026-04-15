tc = int(input())
for _ in range(tc):
    try:
        a, b = map(int, input().split())
        temp = [input().strip() for _ in range(a)]
    except:
        break
    
    output = ""
    for j in range(b):  
        lookup = {}
        for i in range(a):  
            ch = temp[i][j]
            lookup[ch] = lookup.get(ch, 0) + 1

        max_count = max(lookup.values())
        candidates = []
        
        for key, value in sorted(lookup.items()):
            if value == max_count:
                candidates.append(key)

        output += min(candidates)
    
    err = 0
    for char in temp:
        for j in range(b):
            if char[j] != output[j]:
                err += 1
    
    print(output)
    print(err)
