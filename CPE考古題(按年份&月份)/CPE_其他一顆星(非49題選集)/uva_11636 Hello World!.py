tc = 1
while True:
    try:
        n = int(input())
    except:
        break

    if n < 0:
        break

    temp = 1
    count = 0
    while temp < n:
        temp *= 2
        count += 1
    
    print(f"Case {tc}: {count}")
    tc += 1
