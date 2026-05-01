while True:
    try:
        line = input() # 這邊避免掉空行
        if line == "":
            continue
        n = int(line)
    except:
        break
    books = sorted(list(map(int, input().split())))
    target_price = int(input())

    # if tc > 1: 這邊每行通通都要補空行，所以不用管最後一行要不要空
    #     print()

    diff = float("inf")
    left, right = 0, n-1
    temp = [0, 0]
    
    while left < right:
        if books[left] + books[right] > target_price:
            right -= 1
        elif books[left] + books[right] < target_price:
            left += 1
        else:
            if books[right] - books[left] < diff:
                temp[0] = books[left]
                temp[1] = books[right]
                diff = books[right] - books[left]
            left += 1
            right -= 1
            
    # print(temp[0], temp[1])
    print(f"Peter should buy books whose prices are {temp[0]} and {temp[1]}.")
    print()
