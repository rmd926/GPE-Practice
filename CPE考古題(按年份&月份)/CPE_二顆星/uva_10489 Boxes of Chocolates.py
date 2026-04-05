tc = int(input())
for _ in range(tc):
    try:
        N, B = map(int, input().split())
    except:
        break
    
    total = []
    for _ in range(B):
        temp = 1
        try:
            seq = list(map(int, input().split()))
        except:
            break
        
        n = seq[0]
        target = seq[1:]

        for num in target:
            temp *= num

        total.append(temp)
    
    print(sum(total) % N)
