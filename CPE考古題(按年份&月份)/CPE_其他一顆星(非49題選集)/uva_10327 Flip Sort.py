def swap_times(target):
    n = len(target)
    count = 0
    for i in range(n):
        for j in range(n-i-1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
                count += 1
    
    return count

while True:
    try:
        n = int(input())
        target = list(map(int, input().split()))
    except:
        break

    print(f"Minimum exchange operations : {swap_times(target)}")
