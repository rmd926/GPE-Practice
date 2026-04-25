tc = 1
while True:
    try:
        n = int(input())
    except:
        break
    
    if n < 0:
        break
    print(f"Case {tc}:")
    produce = list(map(int, input().split()))
    cost = list(map(int, input().split()))

    cur = n
    for i in range(12):
        if cur >= cost[i]:
            print("No problem! :D")
            cur += (produce[i] - cost[i])
        else:
            print("No problem. :(") # 該次取消，不扣掉庫存題目
            continue
        
    tc += 1
