while True:
    try:
        v, t = map(int, input().split())
        print(2 * v * 2 * t // 2)
    except EOFError:
        break
