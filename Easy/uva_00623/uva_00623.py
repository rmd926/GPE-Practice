import sys
def factorial(n):
    fac = [1] * (n+1)
    for i in range(1, n+1):
        fac[i] = fac[i-1] * i
    return fac[n]

while True:
    try:
        target = int(sys.stdin.buffer.readline())
    except:
        break
    
    print(f"{target}!")
    print(factorial(target))