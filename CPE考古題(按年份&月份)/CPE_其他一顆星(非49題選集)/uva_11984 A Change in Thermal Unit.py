tc = int(input())
for t in range(tc):
    try:
        C, d = map(int, input().split())
    except:
        break
    
    ans = C + d * 5 / 9
    print(f"Case {t+1}: {ans:.2f}")
