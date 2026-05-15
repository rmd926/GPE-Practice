while True:
    target = int(input())
    if target == 0:
        break

    temp = 0
    cur_page = 0

    while temp <= target:
        cur_page += 1
        temp += cur_page
    
    missing = temp - target
    print(missing, cur_page)
