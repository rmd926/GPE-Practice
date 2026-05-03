while True:
    try:
        target = input()
    except:
        break

    ans = ""
    for ch in target:
        ans += chr(ord(ch) - 7)

    print(ans)
