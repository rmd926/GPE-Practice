tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    target = list(map(int, input().split()))
    target = sorted(target)[::-1]
    
    ans = 0
    for i in range(n):
        if i % 3 == 2:
            ans += target[i]
    print(ans)
