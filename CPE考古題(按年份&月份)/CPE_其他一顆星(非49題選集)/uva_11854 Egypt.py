while True:
    try:
        target = list(map(int, input().split()))
    except:
        break

    if target[0] == target[1] == target[2] == 0:
        break

    target.sort()
    if target[0] ** 2 + target[1] ** 2 == target[2] ** 2:
        print("right")
        
    else:
        print("wrong")
