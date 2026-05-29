tc = 1
while True:
    try:
        line = input()
    except:
        break
    
    if line == "":
        continue
    
    n = int(line)
    if n == 0:
        break

    target = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        temp = target[i]
        ans = max(ans, temp)
        for j in range(i+1, n):
            temp *= target[j]
            ans = max(ans, temp)
    
    print(f"Case #{tc}: The maximum product is {ans}.")
    print()
    tc += 1
