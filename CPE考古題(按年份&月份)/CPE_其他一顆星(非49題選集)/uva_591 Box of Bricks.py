tc = 1
while True:
    try:
        n = int(input())
        if n == 0:
            break
        target = list(map(int, input().split()))
    except:
        break

    if tc > 1:
        print()
    print(f"Set #{tc}")

    temp = 0
    avg = sum(target) // n

    for num in target:
        temp += abs(num-avg)
    
    ans = temp // 2
    print(f"The minimum number of moves is {ans}.")

    tc += 1
