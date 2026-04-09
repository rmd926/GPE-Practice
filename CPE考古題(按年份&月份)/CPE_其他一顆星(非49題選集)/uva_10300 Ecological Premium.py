tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    total = 0
    for _ in range(n):
        a, b, c = map(int, input().split())
        total += a*c
    
    print(total)
