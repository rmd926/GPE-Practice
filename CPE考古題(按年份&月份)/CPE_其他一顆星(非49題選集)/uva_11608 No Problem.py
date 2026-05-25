TC = 1

while True:
    n = int(input())
    if n == -1:
        break
    
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    
    print(f'Case {TC}:')
    cur = n
    for i in range(len(a)):
        if cur >= b[i]: # 庫存夠的case
            print('No problem! :D')
            cur -= b[i] # 調整當前庫存，扣除使用
        
        else:
            print('No problem. :(')
        cur += a[i] # 調整當前庫存，加上該月的生產
    TC += 1
