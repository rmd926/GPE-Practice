mapping = {"0": "O", "1": "I", "2": "Z", "3": "E",  "4": "A", "5": "S", "6": "G", "7": "T", "8": "B", "9": "P"}

tc = int(input())
for t in range(tc):
    while True:
        try:
            line = input()
        except:
            break
        if line == "":
            break

        ans = ""
        for ch in line:
            if ch in mapping:
                ans += mapping[ch]
            else:
                ans += ch

        print(ans)
        if t+1 != tc:
            print()
