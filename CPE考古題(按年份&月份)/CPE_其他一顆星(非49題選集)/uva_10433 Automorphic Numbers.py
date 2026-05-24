while True:
    try:
        target = input()
    except:
        break

    num = int(target)
    if num == 0 or num == 1:
        print("Not an Automorphic number.")
        continue

    n = len(target)

    square = num ** 2
    if num == int(str(square)[-n:]):
        print(f"Automorphic number of {n}-digit.")
    else:
        print("Not an Automorphic number.")

# 2026.05.25 二刷，要注意輸入可能會有前導0的這種測資，因此input必須是字串格式，再用num去轉。另外 n-digit這種Output，n就是input的字串長度，和轉成num的長度不要混用。
