while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n < 0:
        break

    pizza = 1 + n*(n+1) // 2
    print(f"{pizza}")