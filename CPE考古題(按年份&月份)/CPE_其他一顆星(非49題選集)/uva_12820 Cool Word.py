case = 1
while True:
    try:
        tc = int(input())
    except:
        break
    
    count = 0
    for _ in range(tc):
        target = input()
        lookup = {}
        
        for char in target:
            if char not in lookup:
                lookup[char] = 1
            else:
                lookup[char] += 1
        
        temp = []
        for key, value in sorted(lookup.items()):
            temp.append(value)
        
        if len(temp) >= 2 and len(temp) == len(set(temp)):
            count += 1
        
    print(f"Case {case}: {count}")

    case += 1
