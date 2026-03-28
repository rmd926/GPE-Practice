def calc(name):
    total = 0
    
    for ch in name:
        if 'a' <= ch <= 'z':
            total += ord(ch) - ord('a') + 1
        elif 'A' <= ch <= 'Z':
            total += ord(ch) - ord('A') + 1
    
    while total >= 10:
        s = 0
        while total > 0:
            s += total % 10
            total //= 10
        total = s
    
    return total

while True:
    try:
        name1 = input()
        name2 = input()
    except EOFError:
        break
    
    n1 = calc(name1)
    n2 = calc(name2)
    
    if n1 > n2:
        n1, n2 = n2, n1
    
    if n2 == 0:
        print("0.00 %")
    else:
        print(f"{n1 * 100 / n2:.2f} %")
