lookup = {}
while True:
    try:
        line = input().lower()
    except:
        break

    word = ""
    for ch in line:
        if ch.isalpha():
            word += ch
        else:
            if word != "":
                if word not in lookup:
                    lookup[word] = 1
                else:
                    lookup[word] += 1
                word = ""

    if word != "":
        if word not in lookup:
            lookup[word] = 1
        else:
            lookup[word] += 1
    
for key, value in sorted(lookup.items()):
    print(key)
