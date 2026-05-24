tc = int(input())
for _ in range(tc):
    num = int(input())
    count = 1

    temp = num
    while True:
        temp += int(str(temp)[::-1])
        if str(temp) != str(temp)[::-1]:
            count += 1
        else:
            break
    
    print(f"{count} {temp}")

# 2026.05.24 二刷
