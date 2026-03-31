tc = 1
while True:
    try:
        line = input()
    except:
        break

    if line == "":
        continue

    n = int(line)
    target = list(map(int, input().split()))
    ans = 0

    for i in range(n):
        temp = target[i]
        if temp > ans:
            ans = temp
        for j in range(i + 1, n):
            temp *= target[j]
            if temp > ans:
                ans = temp

    print(f"Case #{tc}: The maximum product is {ans}.")
    print()

    tc += 1
