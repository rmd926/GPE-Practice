while True:
    try:
        n = int(input())
    except:
        break
    
    if n < 0:
        break

    ans = ''
    if n == 0:
        ans = '0'
    
    while n > 0:
        ans = str(n % 3) + ans
        n //= 3

        '''
        n = 10 ans = '1'
        n = 3 ans = '10'
        n = 1 ans = '101'
        n = 0 out of while loop
        '''
    print(ans)