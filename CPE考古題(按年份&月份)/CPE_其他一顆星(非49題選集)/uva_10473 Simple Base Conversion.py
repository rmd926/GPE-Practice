while True:
    try:
        target = input()
    except:
        break
    
    if target == "-1":
        break
    if target[0:2] == "0x" or target[0:2] == "0X":
        print(int(target, 16))
    else:
        print("0x" + hex(int(target))[2:].upper())

# 2026.05.25 二刷
