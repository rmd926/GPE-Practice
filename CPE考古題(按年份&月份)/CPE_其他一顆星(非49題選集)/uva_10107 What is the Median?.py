temp = []
while True:
    try:
        num = int(input())
    except:
        break

    temp.append(num)
    temp.sort()

    mid = len(temp) // 2

    if len(temp) % 2 == 0:
        print((temp[mid-1] + temp[mid]) // 2)
    else:
        print(temp[mid])
# 2026.05.24 二刷
