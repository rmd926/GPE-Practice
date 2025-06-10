while True:
    target = input()
    if target == '0':
        break

    odd, even = 0, 0

    for i in range(0, len(target), 2):
        odd += int(target[i])
    
    for j in range(1, len(target), 2):
        even += int(target[j])

    if abs(odd - even) % 11 == 0:
        print(f"{target} is a multiple of 11.")
    else:
        print(f"{target} is not a multiple of 11.")