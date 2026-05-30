tc = int(input())
for _ in range(tc):
    try:
        seq = list(map(int, input().split()))
    except:
        break

    total = sum(seq)
    if total % 2 != 0:
        print("NO")
        continue

    target = total // 2
    dp = [False] * (target+1)
    dp[0] = True

    for num in seq:
        for i in range(target, num-1, -1):
            if dp[i-num]:
                dp[i] = True
    
    if dp[target]:
        print("YES")
    else:
        print("NO")
