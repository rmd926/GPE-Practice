tc = int(input())
for t in range(tc):
    try:
        target = int(input())
    except:
        break

    temp = []
    new_target = target

    while new_target not in temp and new_target != 1:
        temp.append(new_target)
        digit_sum = 0
        for digit in str(new_target):
            digit_sum += int(digit) ** 2
            
        new_target = digit_sum

    if new_target == 1:
        print(f"Case #{t+1}: {target} is a Happy number.")
    else:
        print(f"Case #{t+1}: {target} is an Unhappy number.")
