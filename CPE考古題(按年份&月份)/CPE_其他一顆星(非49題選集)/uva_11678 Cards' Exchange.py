while True:
    try:
        a, b = map(int, input().split())
    except:
        break
    if a == b == 0:
        break

    A = set(list(map(int, input().split())))
    B = set(list(map(int, input().split())))
    K = A & B

    print(min(len(A), len(B)) - len(K))
