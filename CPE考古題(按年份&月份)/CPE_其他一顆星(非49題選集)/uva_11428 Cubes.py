while True:
    n = int(input())
    if n == 0:
        break

    found = False

    for y in range(1, 101):
        target = n + y ** 3
        x = round(target ** (1 / 3))

        if x > 0 and x ** 3 == target:
            print(x, y)
            found = True
            break

    if not found:
        print("No solution")
