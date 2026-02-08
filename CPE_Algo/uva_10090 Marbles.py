import math

while True:
    try:
        target = int(input())
    except EOFError:
        break
    if target == 0:
        break

    c1, n1 = map(int, input().split())
    c2, n2 = map(int, input().split())

    min_cost = float("inf")
    cost = 0
    count1, count2 = 0, 0
    ans = []

    d = math.gcd(n1, n2)
    if target % d != 0:
        print("failed")
        continue

    # box1 priority
    if (c1 / n1) < (c2 / n2):
        count1 = target // n1
        while count1 >= 0:
            remain = target - count1 * n1
            if remain % n2 == 0:
                count2 = remain // n2
                cost = count1 * c1 + count2 * c2
                ans.append((count1, count2))
                break
            count1 -= 1

    # box2 priority
    elif (c1 / n1) > (c2 / n2):
        count2 = target // n2
        while count2 >= 0:
            remain = target - count2 * n2
            if remain % n1 == 0:
                count1 = remain // n1
                cost = count1 * c1 + count2 * c2
                ans.append((count1, count2))
                break
            count2 -= 1

    if ans:
        print(ans[-1][0], ans[-1][1])
    else:
        print("failed")
