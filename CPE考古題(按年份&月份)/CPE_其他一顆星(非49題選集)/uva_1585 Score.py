tc = int(input())
for _ in range(tc):
    try:
        target = input()
    except:
        break

    combo = 0
    score = 0

    for ch in target:
        if ch == "O":
            combo += 1
            score += combo
        elif ch == "X":
            combo = 0
        
    print(score)
