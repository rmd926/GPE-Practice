while True:
    try:
        target = input().strip()
    except EOFError:
        break

    palindromes = set()
    n = len(target)

    # 枚舉所有連續子字串
    for i in range(n):
        for j in range(i+1, n+1):
            sub = target[i:j]
            if sub == sub[::-1]:
                palindromes.add(sub)

    print(f"The string '{target}' contains {len(palindromes)} palindromes.")
