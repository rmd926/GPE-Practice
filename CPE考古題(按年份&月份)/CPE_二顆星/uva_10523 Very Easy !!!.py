while True:
    try:
        N, A = map(int, input().split())
    except:
        break

    ans = 0
    for i in range(1, N+1):
        ans += i * A ** i
    
    print(ans)
