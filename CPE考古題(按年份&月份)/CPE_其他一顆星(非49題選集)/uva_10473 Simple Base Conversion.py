while True:
    try:
        target = input().strip()
    except EOFError:
        break

    if target == "-1":
        break

    if target.startswith("0x") or target.startswith("0X"):
        print(int(target, 16))
    else:
        print("0x" + hex(int(target))[2:].upper())
