while True:
    try:
        n = int(input())
    except:
        break
    
    if n == 0:
        break
    
    target = list(map(int, input().split()))
    cur = target[0]
    ans = 0

    for i in range(1, n):
        ans += abs(cur)
        cur += target[i]
    
    print(ans)
