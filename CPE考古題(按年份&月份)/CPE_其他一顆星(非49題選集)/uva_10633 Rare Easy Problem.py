while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    ans = []
    ans.append(n + n // 9)

    if n % 9 == 0:
        ans.append(n + n // 9 - 1)
    
    ans.sort()
    print(*ans)

# 2026.05.25 二刷 輸出前記得sort
