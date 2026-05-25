tc = int(input())
for t in range(tc):
    try:
        s1 = input()
        s2 = input()
    except:
        break

    if s1 == s2:
        print(f"Case {t+1}: Yes")
    
    elif s1.replace(" ", "") == s2 or s1 == s2.replace(" ", ""):
        print(f"Case {t+1}: Output Format Error")
    
    else:
        print(f"Case {t+1}: Wrong Answer")

# 2026.05.26 二刷
