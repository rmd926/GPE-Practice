while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    
    ans = 0
    temp = 0
    while a > 0 and b > 0:
        if a % 10 + b % 10 + temp >= 10:
            ans += 1
            temp = 1
        else:
            temp = 0
        
        a //= 10
        b //= 10
    
    if ans == 0:
        print("No carry operation.")
    elif ans == 1:
        print("1 carry operation.")
    else:
        print(f"{ans} carry operations.")