def factor_sum(target: int):
    ans = 0
    for num in range(1, target//2 + 1):
        if target % num == 0:
            ans += num

    return ans

tc = int(input())
for _ in range(tc):
    try:
        target = int(input())
    except:
        break

    if target == factor_sum(target):
        print("perfect")
    
    elif target > factor_sum(target):
        print("deficient")
    
    else:
        print("abundant")
