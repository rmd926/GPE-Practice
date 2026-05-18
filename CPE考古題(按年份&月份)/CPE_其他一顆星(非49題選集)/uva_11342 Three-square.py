tc = int(input())
targets = []

for _ in range(tc):
    targets.append(int(input()))

max_target = max(targets)

ans = [None] * (max_target + 1)

limit = int(max_target ** 0.5) + 1

for a in range(0, limit + 1):
    for b in range(a, limit + 1):
        for c in range(b, limit + 1):
            total = a ** 2 + b ** 2 + c ** 2

            if total > max_target:
                break

            if ans[total] is None:
                ans[total] = (a, b, c)

for target in targets:
    if ans[target] is None:
        print(-1)
    else:
        a, b, c = ans[target]
        print(a, b, c)
