tc = int(input())
for t in range(tc):
    try:
        n = int(input())
        target = input()
    except:
        break

    ans = 0
    idx = 0

    while idx < n:
        if target[idx] == ".":
            ans += 1
            idx += 2
        
        idx += 1
    
    print(f"Case {t+1}: {ans}")
