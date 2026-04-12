while True:
    try:
        target = list(map(int, input().split()))
    except:
        break

    cur = 0
    max_ans = 0

    for i in range(len(target)):
        cur = max(0, cur + target[i])
        max_ans = max(max_ans, cur)
        
    print(max_ans)
