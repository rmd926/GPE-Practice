tc = int(input())
for t in range(tc):
    try:
        N = int(input())
    except:
        break
    
    record = [] # 把所有郵票類型放在這邊
    backup = [] # 以子List記錄每個人所擁有的郵票
    for _ in range(N):
        seq = list(map(int, input().split()))
        target = list(set(seq[1:]))
        backup.append(target) # [[1, 2, 3], [4, 5], [4, 2, 6]]

        for num in target:
            record.append(num) # [1, 2, 3, 4, 5, 4, 2, 6]
    
    unique = [] # 只存放unique的郵票，只要有出現過重複次數的郵票就會被丟棄
    for num in record:
        if record.count(num) == 1:
            unique.append(num) # [1, 2, 3, 4, 5, 4, 2, 6] - > [1, 3, 5, 6]
    
    print(f"Case {t+1}: ", end="")

    if len(unique) == 0:   # 只要沒有任何一張unique郵票就是 0 %，避免掉 divide by 0。
        for _ in range(N):
            print("0.000000%", end=" ")

    for back in backup:
        count = 0
        for i in range(len(back)):
            if back[i] in unique:
                count += 1
        
        print(f"{100 * count / len(unique):.6f}%", end=" ")
    print()
