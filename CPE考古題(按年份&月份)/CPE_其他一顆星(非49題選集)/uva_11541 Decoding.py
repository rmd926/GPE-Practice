tc = int(input())
for t in range(tc):
    target = input()

    letter_temp = ""
    digit_temp = ""
    ans = ""

    for ch in target:
        if ch.isalpha():
            if digit_temp:
                ans += letter_temp * int(digit_temp)
                letter_temp = ""
                digit_temp = ""
            letter_temp += ch
    
        elif ch.isdigit():
            digit_temp += ch
    
    if letter_temp and digit_temp:
        ans += letter_temp * int(digit_temp)
    
    print(f"Case {t+1}: {ans}")

# 2026.05.25 二刷
