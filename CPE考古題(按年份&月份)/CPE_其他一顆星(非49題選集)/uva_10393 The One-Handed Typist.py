mapping = {
    1: "qaz",
    2: "wsx",
    3: "edc",
    4: "rfvtgb",
    7: "yhnujm",
    8: "ik",
    9: "ol",
    10: "p"
}

while True:
    try:
        N, M = map(int, input().split())
    except:
        break

    banned_num = []

    while len(banned_num) < N:
        banned_num += list(map(int, input().split()))
    
    max_length = float('-inf')
    ans = set()
    banned_string = ""
    for num in banned_num:
        if num in mapping.keys():
            banned_string += mapping[num]
        else:
            continue

    for _ in range(M):
        try:
            target = input()
        except:
            break

        status = True
        for ch in target:
            if ch in banned_string:
                status = False
                break
            else:
                continue

        if status:
            if len(target) > max_length:
                ans = set()
                ans.add(target)
                max_length = len(target)
            elif len(target) == max_length:
                ans.add(target)
            else:
                ans = ans
        
    print(len(ans))
    for word in sorted(ans):
        print(word)
