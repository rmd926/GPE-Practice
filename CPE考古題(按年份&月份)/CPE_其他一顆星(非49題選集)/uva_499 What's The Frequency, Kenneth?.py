while True:
    try:
        line = input()
        if line == "":
            break
    except:
        break

    lookup = {}
    for ch in line:
        if ch.isalpha():
            if ch not in lookup:
                lookup[ch] = 1
            else:
                lookup[ch] += 1
        else:
            continue
    
    max_value = max(lookup.values())
    ans = ""
    for key, value in sorted(lookup.items()):
        if value == max_value:
            ans += key
    print(f"{ans} {max_value}")
