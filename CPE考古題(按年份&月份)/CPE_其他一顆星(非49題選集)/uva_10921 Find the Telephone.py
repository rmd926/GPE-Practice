while True:
    try:
        target = input()
    except:
        break

    ans = ""
    for ch in target:
        if ch in "ABC":
            ans += "2"

        elif ch in "DEF":
            ans += "3"

        elif ch in "GHI":
            ans += "4"

        elif ch in "JKL":
            ans += "5"

        elif ch in "MNO":
            ans += "6"

        elif ch in "PQRS":
            ans += "7"

        elif ch in "TUV":
            ans += "8"

        elif ch in "WXYZ":
            ans += "9"

        else:
            ans += ch
            
    print(ans)
