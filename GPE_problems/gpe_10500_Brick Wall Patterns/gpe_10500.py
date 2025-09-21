def fibonacci_dp(n: int):
    fib = [0] * (n+1)
    fib[0] = 1
    fib[1] = 1
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        break
    print(fibonacci_dp(n))
