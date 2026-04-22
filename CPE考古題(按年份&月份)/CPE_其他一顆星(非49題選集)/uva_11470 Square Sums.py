tc = 1
while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    target = []
    for _ in range(n):
        line = list(map(int, input().split()))
        target.append(line)
    
    layer = (n+1) // 2
    ans = []
    for k in range(layer):
        total = 0
        for i in range(k, n-k):
            for j in range(k, n-k):
                if i == k or i == n-k-1 or j == k or j == n-k-1:
                    total += target[i][j]
        ans.append(total)
    
    print(f"Case {tc}: ", end = "")
    print(*ans)

    tc += 1
