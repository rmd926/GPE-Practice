while True:
    N, D = map(int, input().split())
    if N+D == 0:
        break
    print(N**D)