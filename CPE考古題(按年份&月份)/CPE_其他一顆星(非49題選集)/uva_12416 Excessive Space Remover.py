while True:
    try:
        target = input()
    except:
        break

    count = 0
    temp = []
    for ch in target:
        if ch == " ": # 遇到空格就+1
            count += 1
        
        else: 
            if count > 0: # 遇到非空格時先把當前count丟到temp list中隨後把count歸零，且若count為0時則continue
                temp.append(count)
                count = 0
            else:
                continue
    
    max_space = max(temp) # 取出最大的連續空格數，接著用一個while loop秒掉這題
    ans = 0
    while max_space > 1:
        remain = max_space % 2
        max_space = max_space // 2 + remain
        ans += 1
    
    print(ans)
