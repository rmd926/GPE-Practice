while True:
    try:
        x1, y1, x2, y2 = map(int, input().split())
    except:
        break
    if x1 == y1 == x2 == y2 == 0:
        break

    if abs(x1 - x2) == abs(y1 - y2) == 0:
        print(0)
    
    elif abs(x1 - x2) == abs(y1 - y2) and abs(x1 - x2) != 0:
        print(1)
    
    elif abs(x1 - x2) == 0 and abs(y1 - y2) != 0 or abs(x1 - x2) != 0 and abs(y1 - y2) == 0:
        print(1)
    
    elif abs(x1 - x2) != 0 and abs(y1 - y2) != 0 and abs(x1 - x2) != abs(y1 - y2):
        print(2)
