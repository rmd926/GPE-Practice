tc = int(input())
for _ in range(tc):
    target = []
    ans = 0
    while True:
        try:
            n = int(input())
        except:
            break

        if n == 0:
            break

        target.append(n)
        target = sorted(target)[::-1]
    
    for i in range(len(target)):
        ans += 2 * (target[i]) ** (i+1)
    
    if ans > 5000000:
        print("Too expensive")
    else:
        print(ans)
