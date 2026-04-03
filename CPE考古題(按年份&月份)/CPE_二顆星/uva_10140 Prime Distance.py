import math

MAX = int(math.sqrt(2147483647)) + 1
is_prime = [True] * (MAX + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(MAX ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i ** 2, MAX + 1, i):
            is_prime[j] = False

prime = []
for i in range(2, MAX + 1):
    if is_prime[i]:
        prime.append(i)

while True:
    try:
        low, high = map(int, input().split())
    except EOFError:
        break

    seg = [True] * (high - low + 1)

    for p in prime:
        if p * p > high:
            break

        start = max(p * p, ((low + p - 1) // p) * p)
        for j in range(start, high + 1, p):
            seg[j - low] = False

    if low == 1:
        seg[0] = False

    target = []
    for num in range(low, high + 1):
        if seg[num - low]:
            target.append(num)

    if len(target) < 2:
        print("There are no adjacent primes.")
    else:
        min_diff = float("inf")
        max_diff = float("-inf")
        min_ans = []
        max_ans = []

        for i in range(1, len(target)):
            gap = target[i] - target[i - 1]

            if gap < min_diff:
                min_diff = gap
                min_ans = [target[i - 1], target[i]]

            if gap > max_diff:
                max_diff = gap
                max_ans = [target[i - 1], target[i]]

        print(f"{min_ans[0]},{min_ans[1]} are closest, {max_ans[0]},{max_ans[1]} are most distant.")
