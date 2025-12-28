while True:
    target = list(map(int, input().split()))
    if sum(target) == 0:
        break
    print((60 * (target[2] - target[0]) + target[3] - target[1]) % 1440)