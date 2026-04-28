while True:
    try:
        n = int(input())
    except:
        break

    half = 10 ** (n // 2)
    limit = 10 ** n

    for i in range(2 * half):
        num = i * i

        if num >= limit:
            continue

        left = num // half
        right = num % half

        if left + right == i:
            print(f"{num:0{n}d}")
