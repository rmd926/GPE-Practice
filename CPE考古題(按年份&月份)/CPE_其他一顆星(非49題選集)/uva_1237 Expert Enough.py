tc = int(input())
for t in range(tc):
    n = int(input())
    lookup = {}
    
    for _ in range(n):
        brand, low, high = map(str, input().split())
        lookup[brand] = int(low), int(high)

    Q = int(input())
    for _ in range(Q):
        price = int(input())
        count = 0

        for key, value in lookup.items():
            if value[0] <= price <= value[1]:
                count += 1
                ans = key
        
        if count == 1:
            print(ans)

        else:
            print("UNDETERMINED")
    
    if t+1 < tc:
        print()
