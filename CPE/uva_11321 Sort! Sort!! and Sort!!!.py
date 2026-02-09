def mod(x, m):
    return x - int(x / m) * m

while True:
    n, m = map(int, input().split())
    print(n, m)
    if n == 0 and m == 0:
        break

    nums = []
    for _ in range(n):
        nums.append(int(input()))

    def sorting(x):
        r = mod(x, m)
        if x % 2 != 0:          # odd
            return (r, 0, -x)   # odd first, larger first
        else:                   # even
            return (r, 1, x)    # even later, smaller first

    nums.sort(key=sorting)

    for x in nums:
        print(x)