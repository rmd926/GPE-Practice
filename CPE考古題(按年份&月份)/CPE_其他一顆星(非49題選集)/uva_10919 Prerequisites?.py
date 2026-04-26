while True:
    try:
        k, m = map(int, input().split())
    except:
        break
    
    if k == 0:
        break

    lookup = list(map(int, input().split()))
    status = True
    
    for _ in range(m):
        count = 0
        seq = list(map(int, input().split()))

        for num in lookup:
            if num in seq[2:]:
                count += 1
            else:
                continue

        if count >= seq[1]:
            continue
        else:
            status = False

    if status:
        print("yes")
    else:
        print("no")
