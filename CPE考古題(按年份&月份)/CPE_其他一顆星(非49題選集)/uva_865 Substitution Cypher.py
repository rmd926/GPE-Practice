tc = int(input())
space = input()

for t in range(tc):
    try:
        s1 = input()
        s2 = input()
    except:
        break

    lookup = {}
    for i in range(len(s1)):
        lookup[s1[i]] = s2[i]

    print(s2)
    print(s1)
    while True:
        try:
            line = input()
        except:
            break
        
        if line == "":
            break

        temp = ""
        for ch in line:
            if ch in lookup:
                temp += lookup[ch]
            else:
                temp += ch
        
        print(temp)

    if t+1 < tc:
        print()
