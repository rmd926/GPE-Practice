while True:
    try:
        target = int(input())
    except:
        break

    if target == 0:
        break

    record = []

    while target not in record:
        record.append(target)
        target = ((target ** 2) // 100) % 10000
        
    print(len(record))
# 2026.05.25 二刷
