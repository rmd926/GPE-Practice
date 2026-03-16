tc = int(input())
for _ in range(tc):
    n = int(input())
    target = list(map(int, input().split()))
    stack = [target[0]]

    for i in range(1, n - 1):
        if target[i+1] - target[i] > sum(stack):
            stack.append(target[i])

    stack.append(target[-1])

    print(len(stack))
