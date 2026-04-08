tc = int(input())
for t in range(tc):
    try:
        seq = list(map(int, input().split()))
    except:
        break

    n = seq[0]
    target = seq[1:]

    print(f"Case {t+1}: {target[n//2]}")
