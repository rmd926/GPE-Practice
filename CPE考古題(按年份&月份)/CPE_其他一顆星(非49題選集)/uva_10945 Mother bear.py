while True:
    try:
        target = input()
    except:
        break
    if target == "DONE":
        break

    target = target.lower()
    temp = ""
    for char in target:
        if char.isalpha():
            temp += char
        else:
            continue
    
    if temp == temp[::-1]:
        print("You won't be eaten!")

    else:
        print("Uh oh..")
