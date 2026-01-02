while True:
    target = input()
    if target == "0":
        break

    elif target == '9':
        print(f"{target} is a multiple of 9 and has 9-degree 1.")

    elif int(target) % 9 == 0:
        count = 0
        new_num = target
        while int(new_num) != 9:
            count += 1
            temp = 0
            for i in new_num:
                temp += int(i)
            new_num = str(temp)
        print(f"{target} is a multiple of 9 and has 9-degree {count}.")
    
    else:
        print(f"{target} is not a multiple of 9.")