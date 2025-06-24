n = int(input())

for i in range(n):
    a = [int(i) for i in input().split()]
    if a[2] - a[1] == a[1] - a[0] and a[3] - a[1] == 2 * (a[2] - a[1]):
        a.append(a[3] + a[3] - a[2])
    else: # 等比
        a.append(a[3] * (a[3] // a[2]))
    print(*a)