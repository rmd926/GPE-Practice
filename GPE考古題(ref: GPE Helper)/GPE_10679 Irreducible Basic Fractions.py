def sol(num: int):
    ans = num
    div = 2

    while div * div <= num:
        if num % div == 0:
            ans -= ans // div

            while num % div == 0:
                num //= div
        
        if div == 2:
            div = 3
        else:
            div += 2
        
    if num > 1:
        ans -= ans // num
    
    return ans

while True:
    try:
        num = int(input())
    except:
        break

    if num == 0:
        break
    
    print(sol(num))
