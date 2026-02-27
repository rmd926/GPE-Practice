tc = int(input())

for t in range(tc):
    space = input()
    
    d2, m2, y2 = map(int, input().split("/"))  # today
    d1, m1, y1 = map(int, input().split("/"))  # birth

    if y1 > y2 or (y1 == y2 and m1 > m2) or (y1 == y2 and m1 == m2 and d1 > d2):
        print(f"Case #{t+1}: Invalid birth date")
        continue
    
    else:
        age = y2 - y1
        if m2 < m1 or (m2 == m1 and d2 < d1):
            age -= 1

        if age > 130:
            print(f"Case #{t+1}: Check birth date")
        else:
            print(f"Case #{t+1}: {age}")
