while True:
    try:
        x = int(input())
        y = int(input())
    except EOFError:
        break

    print(x*y)
