tc = int(input())
for _ in range(tc):
    try:
        s1 = input()
        s2 = input()
    except:
        break

    for ch in s1:
        if ch in "aeiou":
            s1 = s1.replace(ch, "*")

    for ch in s2:
        if ch in "aeiou":
            s2 = s2.replace(ch, "*")

    if s1 == s2:
        print("Yes")
    else:
        print("No")
