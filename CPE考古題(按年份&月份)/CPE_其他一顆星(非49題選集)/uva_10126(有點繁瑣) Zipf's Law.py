tc = 0

while True:
    try:
        n = int(input())   # occur times
    except:
        break

    lookup = {}

    while True:
        line = input()
        if line == "EndOfText":
            break

        temp = ""
        for ch in line.lower():
            if ch.isalpha():
                temp += ch
            else:
                if temp != "":
                    if temp not in lookup:
                        lookup[temp] = 1
                    else:
                        lookup[temp] += 1
                    temp = ""

        if temp != "":
            if temp not in lookup:
                lookup[temp] = 1
            else:
                lookup[temp] += 1

    if tc > 0:
        print()

    ans = []
    for key, value in sorted(lookup.items()):
        if value == n:
            ans.append(key)

    if len(ans) == 0:
        print("There is no such word.")
    else:
        for word in ans:
            print(word)

    tc += 1
