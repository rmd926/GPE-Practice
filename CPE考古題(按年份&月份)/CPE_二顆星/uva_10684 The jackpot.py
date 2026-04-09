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
