tc = int(input())

for _ in range(tc):
    try:
        target = input()
    except:
        break

    h, m = map(int, target.split(":"))

    if h == 12:
        h = 0

    cur = h * 60 + m
    total = 720 - cur

    if total == 0:
        total = 720

    hour = total // 60
    minute = total % 60

    if hour == 0:
        hour = 12
    
    if hour < 10:
        hour = "0" + str(hour)
    
    if minute < 10:
        minute = "0" + str(minute)

    print(f"{hour}:{minute}")
