while True:
    try:
        n = int(input())
    except:
        break

    temp = []
    for _ in range(n):
        temp.append(int(input()))
    
    temp.sort()
    mid_left = temp[(n-1)//2]
    mid_right = temp[n//2]

    count = 0
    for num in temp:
        if num == mid_left or num == mid_right:
            count += 1
    
    case = mid_right - mid_left + 1
    print(f"{mid_left} {count} {case}")
