tc = int(input())
for t in range(tc):
    try:
        target = input()
    except:
        break

    ans = ""
    alpha_temp = ""
    digit_temp = ""

    for i in range(len(target)):
        if target[i].isalpha():
            
            if digit_temp:
                ans += alpha_temp * int(digit_temp)
                digit_temp = ""
                alpha_temp = ""

            alpha_temp += target[i]

        elif target[i].isdigit():
            digit_temp += target[i]

    if digit_temp and alpha_temp:
        ans += alpha_temp * int(digit_temp)
    
    print(f"Case {t+1}: {ans}")
