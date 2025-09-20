def factorial(n: int):
    # 修正：長度用 n+1，從 1 乘到 n；fac[0] = 1
    fac = [1] * (n + 1)
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
    return fac[n]

first = True
while True:
    try:
        line = input()
    except EOFError:
        break
    
    '''
    必須加入空行判斷，這題難度不高，但是輸入輸出很靠北
    但是本題不能用math.comb()，因為onlinejudge python version < 3.8
    '''
    line = line.strip()
    if not line:          # 空行跳過
        continue

    n = int(line)
    # Catalan(n) = C(2n, n) // (n+1)
    ans = factorial(2 * n) // (factorial(n) * factorial(n) * (n + 1))
    

    if not first:
        print() # 兩個測資中間需要空行
    print(ans)
    first = False