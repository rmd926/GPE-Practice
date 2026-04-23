tc = int(input())
for _ in range(tc):
    try:
        n = int(input())
    except:
        break

    count = 1
    target = n + int(str(n)[::-1]) # 起始先做一次，因為原本就是回文的數字還是要做一次操作

    while str(target) != str(target)[::-1]:
        target += int(str(target)[::-1])
        count += 1
    
    print(f"{count} {target}")
