while True:
    try:
        k, m = map(int, input().split())
    except:
        break
    lookup = list(map(int, input().split()))

    if k == 0:
        break

    status = True
    for _ in range(m):
        seq = list(map(int, input().split()))
        count = 0

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

# 2026.05.25 二刷 細節要注意
