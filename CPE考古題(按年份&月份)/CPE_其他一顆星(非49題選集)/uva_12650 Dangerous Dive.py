while True:
    try:
        N, R = map(int, input().split())
    except:
        break

    target = list(map(int, input().split()))
    gt = [int(x) for x in range(1, N+1)]

    for num in target:
        if num in gt:
            gt.remove(num)
    
    print(*gt) if len(gt) > 0 else print("*")
