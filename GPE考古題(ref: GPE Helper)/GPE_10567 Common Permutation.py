while True:
    try:
        s1 = input()
        s2 = input()
    except:
        break

    ans = ""
    for ch in "abcdefghijklmnopqrstuvwxyz":
        count = min(s1.count(ch), s2.count(ch))
        ans += ch * count

    print(ans)
