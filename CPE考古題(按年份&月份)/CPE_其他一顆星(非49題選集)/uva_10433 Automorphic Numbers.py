while True:
    try:
        target = input()
    except:
        break

    num = int(target)

    if num == 0 or num == 1:
        print("Not an Automorphic number.")
        continue

    square = str(num ** 2)

    if square[-len(target):] == target:
        print(f"Automorphic number of {len(target)}-digit.")
    else:
        print("Not an Automorphic number.")
