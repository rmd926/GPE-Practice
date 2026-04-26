while True:
    try:
        n = int(input())
    except:
        break

    if n < 0:
        break

    if n == 0:
        print(0)
        continue
    
    ans = ""
    while n > 0:
        ans += str(n % 3)
        n //= 3
    
    print(ans[::-1])
