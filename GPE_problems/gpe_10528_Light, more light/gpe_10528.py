# method 1:
while True:
    try:
        n = int(input())
        if n == 0:
            break
        
        if (int(n ** 0.5)**2) == n:  #
            print('yes')
        else:
            print('no')
    except:
        break
# AC 0.340s

# method 2:
import sys, math

# use sys.stdin.read() will be faster
for s in sys.stdin.read().split():
    n = int(s)
    if n == 0:
        break
    r = math.isqrt(n)       
    print('yes' if r*r == n else 'no')

# AC 0.06s
