tc = int(input())
for t in range(tc):
    try:
        n, P, Q = map(int, input().split())
        weight_list = sorted(list(map(int, input().split())))
    except:
        break

    count = 0
    temp_weight = 0
    for weight in weight_list:
        if (weight + temp_weight) <= Q and (count + 1) <= P:
            count += 1
            temp_weight += weight
        else:
            break
    
    print(f"Case {t+1}: {count}")
