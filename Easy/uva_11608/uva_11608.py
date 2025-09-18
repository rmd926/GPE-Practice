TC = 1

while True:
    n = int(input())
    if n == -1:
        break
    
    a = [int(i) for i in input().split()]
    b = [int(i) for i in input().split()]
    
    print(f'Case {TC}:')
    for i in range(len(a)):
        if n >= b[i]: # 庫存夠的case
            print('No problem! :D')
            n -= b[i] # 調整當前庫存，扣除使用
        
        else:
            print('No problem. :(')
        n += a[i] # 調整當前庫存，加上該月的生產
    TC += 1
