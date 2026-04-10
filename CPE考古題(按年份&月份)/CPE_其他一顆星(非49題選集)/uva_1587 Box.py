while True:
    temp = []
    status = True
    try:
        for _ in range(6):
            h, w = map(int, input().split())
            temp.append(h)
            temp.append(w)
    except:
        break
    
    for num in temp:
        if temp.count(num) % 4 != 0:
            status = False
            break
        else:
            continue

    if status:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")
