tc = int(input())
for t in range(tc):
    n = int(input())
    print(f"Case {t+1}:")

    for _ in range(n):
        line = input()
        ans = ""
        prev_is_space = False

        for ch in line:
            if ch == " ":
                if not prev_is_space:
                    ans += ch
                    prev_is_space = True
                else:
                    continue
            else:
                prev_is_space = False
                ans += ch
        
        print(ans)
    
    if t != tc - 1:
        print()
