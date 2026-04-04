tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break
    
    if len(target) != 3:
        print(3)

    else:
        if target[0] == "o" and target[1] == "n" or target[0] == "o" and target[2] == "e" or target[1] == "n" and target[2] == "e":
            print(1)

        else:
            print(2)
