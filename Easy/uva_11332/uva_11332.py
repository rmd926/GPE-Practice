while True:
    target = input()
    if target == '0':
        break
    while int(target) > 9:
        temp = 0
        for i in target:
            temp += int(i)
        target = str(temp)
    print(target)    