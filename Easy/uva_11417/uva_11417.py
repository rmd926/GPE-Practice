import math
while True:
    try:
        n = int(input())
        gcd_sum = 0
        if n == 0:
            break
        else:
            for i in range(1, n):
                for j in range(i+1, n+1):
                    gcd_sum += math.gcd(i,j)
        print(gcd_sum)
    except:
        break

