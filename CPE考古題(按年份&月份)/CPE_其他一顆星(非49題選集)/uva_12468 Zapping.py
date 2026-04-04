while True:
    try:
        low, high = map(int, input().split())
    except:
        break
    
    if low == high == -1:
        break

    ans1 = abs(high - low)
    ans2 = 100 - abs(high - low)

    print(min(ans1, ans2))
