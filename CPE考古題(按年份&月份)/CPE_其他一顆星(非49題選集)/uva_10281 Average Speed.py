last_time = 0
distance = 0
speed = 0
while True:
    try:
        target = input().split() # 會有時間 or 時間 速度這兩種case
    except:
        break

    h, m, s = map(int, target[0].split(":"))
    cur_time = h * 3600 + m * 60 + s

    distance += speed * (cur_time - last_time) / 3600
    last_time = cur_time
    
    if len(target) == 2: # 代表速度有改變
        speed = int(target[1])
    else: # 速度不變的情況下，會做查詢
        print(f"{target[0]} {distance:.2f} km")
