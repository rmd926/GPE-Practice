while True:
    try:
        n = int(input())
    except:
        break

    if n < 0:
        break

    print(n*(n+1) // 2 + 1)
# 2026.05.24 二刷 就單純的切蛋糕公式 
