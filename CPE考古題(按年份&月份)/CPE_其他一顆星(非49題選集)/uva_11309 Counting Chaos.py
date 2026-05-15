tc = int(input())
for _ in range(tc):
    h, m = map(int, input().split(":"))
    cur = 60 * h + m

    while True:
        cur += 1
        if cur >= 1440:
            cur %= 1440
        
        hour = cur // 60
        minute = cur % 60

        if hour == 0:
            temp = str(minute)

        else:
            temp = str(hour) + f"{minute:02d}"
        
        if temp == temp[::-1]:
            print(f"{hour:02d}:{minute:02d}")
            break
