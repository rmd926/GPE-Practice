while True:
    N, R = map(int, input().split())
    all_vol = [int(x) for x in range(1, N+1)]
    return_vol_num = list(map(int,input().split()))

    if N == R:
        print("*")
    else:
        rest = set(all_vol) - set(return_vol_num)
        print(*rest,"")