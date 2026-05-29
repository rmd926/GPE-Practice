import sys

seq = list(map(int, sys.stdin.read().split()))
index = 0

while True:
    n = seq[index]
    index += 1

    if n == 0:
        break

    target = []

    for _ in range(n):
        target.append(seq[index])
        index += 1

    temp_sum = 0
    max_sum = 0

    for num in target:
        temp_sum += num

        if temp_sum < 0:
            temp_sum = 0

        max_sum = max(max_sum, temp_sum)

    if max_sum > 0:
        print(f"The maximum winning streak is {max_sum}.")
    else:
        print("Losing streak.")

'''
while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    target = list(map(int, input().split()))

    current = 0
    max_coins = float('-inf')

    for i in range(len(target)):
        current = max(target[i], target[i] + current)
        max_coins = max(current, max_coins)
    
    if max_coins > 0:
        print(f"The maximum winning streak is {max_coins}.")
    
    else:
        print("Losing streak.")
'''
