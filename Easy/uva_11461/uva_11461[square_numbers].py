while True:
    try:
        x, y =map(int,input().split())
        if x == 0 and y == 0:
            break

        num1 = int(x**0.5)
        num2 = int(y**0.5)

        if (num1**2) != x:
            num1 += 1
        print(num2-num1+1)
    except:
        break
