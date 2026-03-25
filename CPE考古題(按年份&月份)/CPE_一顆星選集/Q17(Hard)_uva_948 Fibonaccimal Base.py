tc = int(input())

fib = [1, 2]
while fib[-1] <= 100000000:
    fib.append(fib[-1] + fib[-2])

for _ in range(tc):
    target = int(input())
    temp = target
    ans = []
    started = False

    for i in range(len(fib) - 1, -1, -1):
        if fib[i] <= temp:
            ans.append("1")
            temp -= fib[i]
            started = True
        elif started:
            ans.append("0")

    print(f"{target} = {''.join(ans)} (fib)")
