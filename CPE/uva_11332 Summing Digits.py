while True:
    target = input()
    if target == "0":
        break
    
    while int(target) >= 10:
        temp = 0
        for i in target:
            temp += int(i)
        target = str(temp) # 再拿來檢驗temp是否有超過兩位數
    print(target) # 最後只要沒有超過兩位數就會直接打印