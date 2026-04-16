while True:
    try:
        target = input()
    except:
        break

    count = 0
    flag = False

    for ch in target:
        if ch.isalpha():
            if flag == False:
                count += 1
                flag = True
            else:
                continue

        else:
            flag = False
    
    print(count)
