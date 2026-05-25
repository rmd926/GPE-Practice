while True:
    try:
        D, N = map(str, input().split())
    except:
        break

    if N == D == "0":
        break
    
    ans = ""
    for ch in N:
        if ch in D:
            continue
        else:
            ans += ch
    
    if ans == "": # 會有完全顯示不出來的case -> 0
        print(0)
    else:
        print(int(ans))

# 2026.05.26 二刷
