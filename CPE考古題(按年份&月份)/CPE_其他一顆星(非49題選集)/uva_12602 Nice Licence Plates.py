tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break

    letter_value = 0
    digit_value = int(target[4:])

    for i in range(3):
        letter_value += (ord(target[i])-65) * 26 ** (2-i)
    
    if abs(letter_value-digit_value) <= 100:
        print("nice")
    else:
        print("not nice")
