while True:
    try:
        target = int(input())
    except:
        break

    if target == 0:
        break

    ans = []
    ans.append(target + target // 9)

    if target % 9 == 0:
        ans.append(target + target // 9 - 1)
    
    ans.sort()
    print(*ans)
