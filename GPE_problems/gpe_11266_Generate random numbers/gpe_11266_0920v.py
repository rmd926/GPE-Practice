while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        break

    seen = set()
    x = n
    while x not in seen:
        seen.add(x)
        x = ((x * x) // 100) % 10000

    print(len(seen))
