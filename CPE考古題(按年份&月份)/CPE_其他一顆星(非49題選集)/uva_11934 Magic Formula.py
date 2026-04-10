while True:
    try:
        a, b, c, d, L = map(int, input().split())
    except:
        break
    
    if a == b == c == d == L == 0:
        break

    count = 0
    for i in range(0, L+1):
        if (a * (i**2) + b * i + c) % d == 0:
            count += 1
    
    print(count)
