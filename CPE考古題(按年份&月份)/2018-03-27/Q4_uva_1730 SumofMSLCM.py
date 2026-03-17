# while True:
#    target = int(input())
#    
#    if target == 0:
#        break
#   ans = 0
#    for i in range(1, target + 1):
#        ans += (target // i) * i
#    print(ans - 1)

while True:
    target = int(input())
    if target == 0:
        break

    ans = 0
    l = 1
    while l <= target:
        val = target // l
        r = target // val
        # sum(l..r) = (l + r) * (r - l + 1) // 2
        ans += val * ((l + r) * (r - l + 1) // 2)
        l = r + 1

    print(ans - 1)
