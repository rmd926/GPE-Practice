tc = int(input())
space = input()

for t in range(tc):
    total = 0
    lookup = {}

    while True:
        try:
            target = input()
        except EOFError:
            break

        if target == "":
            break

        if target not in lookup:
            lookup[target] = 1
        else:
            lookup[target] += 1
        total += 1

    for key, value in sorted(lookup.items()):
        print(f"{key} {value * 100 / total:.4f}")

    if t != tc - 1:
        print()
