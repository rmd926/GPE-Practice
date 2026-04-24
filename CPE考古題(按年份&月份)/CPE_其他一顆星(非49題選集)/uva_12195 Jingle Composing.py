notes = {"W": 1, "H": 1/2, "Q": 1/4, "E": 1/8, "S": 1/16, "T": 1/32, "X": 1/64}

while True:
    try:
        target = input()
    except:
        break

    if target == "*":
        break
    count = 0
    temp = 0
    
    for ch in target:
        if ch == "/":
            if temp == 1:
                count += 1
            temp = 0
        else:
            temp += notes[ch]

    print(count)
