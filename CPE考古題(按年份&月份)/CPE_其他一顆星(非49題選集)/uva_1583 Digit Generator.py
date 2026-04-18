tc = int(input())
for _ in range(tc):
    try:
        target = int(input())
    except:
        break

    n = len(str(target))
    status = False # 是否找到

    # 不用從太小的0開始找，起始點只要從target - 位數*9開始找就好，但要注意個位數=>所以必須要max(0, target - 9n)
    for num in range(max(0, target - 9*n), target+1): 
        temp = 0
        for ch in str(num):
            temp += int(ch)

        if temp + num == target:
            status = True
            break # 因為從最小的開始找，所以就算有多組解，也能確保第一次找到的答案會是最小解
        else:
            continue
    
    print(num) if status else print(0)
