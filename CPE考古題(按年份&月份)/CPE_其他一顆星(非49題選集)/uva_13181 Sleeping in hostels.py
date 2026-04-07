while True:
    try:
        target = input()
    except:
        break

    allocated = []
    for i in range(len(target)):
        if target[i] == "X":
            allocated.append(i)

    ans = 0

    ans = max(ans, allocated[0] - 1)

    for i in range(1, len(allocated)):
        gap = allocated[i] - allocated[i - 1] - 1
        ans = max(ans, (gap - 1) // 2)

    ans = max(ans, len(target) - allocated[-1] - 2)

    print(ans)
