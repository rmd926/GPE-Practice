tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    target = list(map(int, input().split()))
    ans = 0
    index = 0

    while index < n:
        for i in range(index+1, n):
            if target[index] <= target[i]:
                ans += 1
            else:
                continue
            
        index += 1
    print(ans)
