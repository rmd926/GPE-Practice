tc = int(input())
for t in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break

    target.sort()
    n = len(target)

    print(f"Case {t+1}: {target[n//2]}")
