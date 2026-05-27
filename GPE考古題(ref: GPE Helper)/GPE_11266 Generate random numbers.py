while True:
    try:
        target = int(input())
    except:
        break

    if target == 0:
        break

    temp = []
    while target not in temp:
        temp.append(target)
        target = ((target ** 2) // 100) % 10000
    
    print(len(temp))
