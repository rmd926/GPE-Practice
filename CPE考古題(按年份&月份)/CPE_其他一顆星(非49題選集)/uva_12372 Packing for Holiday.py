tc = int(input())
for t in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    status = True

    for num in target:
        if num > 20:
            status = False
            break
        else:
            continue
    
    if status:
        print(f"Case {t+1}: good")
    else:
        print(f"Case {t+1}: bad")
