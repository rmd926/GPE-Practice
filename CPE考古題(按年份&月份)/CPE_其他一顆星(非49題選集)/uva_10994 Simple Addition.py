def S(n):
    ans = 0
    while n > 0:
        x = n % 10

        ans += (n // 10) * 45
        ans += x * (x+1) // 2

        n //= 10
    
    return ans

while True:
    try:
        p, q = map(int, input().split())
    except:
        break
    
    if p < 0 and q < 0:
        break

    print(S(q) - S(p-1))

'''
while True:
    try:
        p, q = map(int, input().split())
    except:
        break
    
    if p < 0 and q < 0:
        break

    ans = 0
    for num in range(p, q+1):
        if num % 10 == 0:
            ans += (num // 10)
        else:
            ans += (num % 10)
    
    print(ans)
'''
