temp = []
while True:
    try:
        n = int(input())
    except:
        break

    temp.append(n)
    temp.sort()
    mid = len(temp) // 2

    if len(temp) % 2 == 0:
        print((temp[mid-1] + temp[mid]) // 2)
        
    else:
        print(temp[mid])
