soundex_dict = {
    "B": 1, "F": 1, "P": 1, "V": 1,
    "C": 2, "G": 2, "J": 2, "K": 2, "Q": 2, "S": 2, "X": 2, "Z": 2,
    "D": 3, "T": 3,
    "L": 4,
    "M": 5, "N": 5,
    "R": 6
}

while True:
    try:
        target = input()
    except:
        break
    
    prev = 0
    ans = ""
    for ch in target:
        if ch in soundex_dict:
            if soundex_dict[ch] != prev:
                ans += str(soundex_dict[ch])
            else:
                continue
				
            prev = soundex_dict[ch]

        else:
            prev = 0
    
    print(ans)

# 2026.05.25 二刷 用ptr概念去解
