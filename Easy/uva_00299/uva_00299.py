def swap_times(n: int, target: list): 
    '''
    use bubble sort to calculate times of swapping.
    '''
    count = 0
    for i in range(n):
        for j in range(n-i-1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j] # swap
                count += 1
    return count

TC = int(input())
for i in range(TC):
    n = int(input())
    target = list(map(int,input().split()))
    count = swap_times(n, target)
    print(f"Optimal train swapping takes {count} swaps.")
