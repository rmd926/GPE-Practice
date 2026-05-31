while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    lookup = {}
    for _ in range(n):
        target = list(map(int, input().split()))
        target.sort()

        combination = tuple(target)
        
        if combination not in lookup:
            lookup[combination] = 1
        else:
            lookup[combination] += 1
    
    max_value = max(lookup.values())

    ans = 0
    
    for key, value in lookup.items():
        if value == max_value:
            ans += value
    
    print(ans)
