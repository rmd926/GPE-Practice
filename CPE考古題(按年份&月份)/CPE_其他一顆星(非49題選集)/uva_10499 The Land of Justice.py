while True:
    try:
        n = int(input())
    except:
        break

    if n < 0:
        break

    if n == 1:
        print("0%")
    else:
        print(f"{n * 25}%")
