while True:
    V_total, V0 = map(int, input().split())

    if V_total == V0 == 0:
        break

    if V_total <= V0:
        print(0)
        continue
    
    status = True # 預設沒有多組解
    max_length = float('-inf')
    num = 1
    best_num = 1

    while num * V0 < V_total:
        temp_length = num * (V_total - num * V0) # 直接同乘以num並且消根號，不要用小數點去比較==
        if temp_length > max_length:
            max_length = temp_length
            best_num = num
            status = True
        
        elif temp_length == max_length:
            status = False
            break

        num += 1
    
    if status:
        print(best_num)
    else:
        print(0)
