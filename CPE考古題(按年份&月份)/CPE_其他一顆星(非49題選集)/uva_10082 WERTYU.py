keyboard = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"

while True:
    try:
        target = input()
    except:
        break
    ans = ""

    for ch in target:
        if ch in keyboard:
            ans += keyboard[keyboard.index(ch)-1]
        else:
            ans += ch
    
    print(ans)

# 2026.05.24 二刷
