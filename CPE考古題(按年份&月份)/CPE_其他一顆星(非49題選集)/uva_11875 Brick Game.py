tc = int(input())
for t in range(tc):
    try:
        seq = list(map(int, input().split()))
    except:
        break

    n = seq[0]
    target = seq[1:]

    print(f"Case {t+1}: {target[n//2]}")

# 2026.05.26 二刷 找中位數
