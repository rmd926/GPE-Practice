while True:
    try:
        L = int(input())
    except:
        break

    if L == 0:
        break

    target = input()
    D_list = []
    R_list = []
    min_distance = float('inf')
    has_z = False # 用來檢查是否有出現z

    for i in range(len(target)):
        if target[i] == "Z":
            has_z = True
            break

        elif target[i] == "D":
            D_list.append(i)

        elif target[i] == "R":
            R_list.append(i)
        
        else:
            continue

    if has_z:
        print(0)

    elif R_list and D_list:
        for i in range(len(D_list)):
            for j in range(len(R_list)):
                min_distance = min(min_distance, abs(D_list[i] - R_list[j]))
        print(min_distance)
        
    else:
        print(0)
