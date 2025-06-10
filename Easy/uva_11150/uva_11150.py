while True:
    try:
        N = int(input())
        ans = N

        while N >= 3:
            ans += N // 3
            N = N // 3 + N % 3
        
        if N == 2: # has only 2 cola bottles can borrow 1.
            ans += 1
        print(ans)
    except:
        break