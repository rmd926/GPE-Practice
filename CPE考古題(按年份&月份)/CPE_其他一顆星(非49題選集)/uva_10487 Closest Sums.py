case = 1
while True:
    try:
        n = int(input())
    except:
        break

    if n == 0:
        break
    
    target = []
    for _ in range(n):
        num = int(input())
        target.append(num)
    
    target.sort()
    print(f"Case {case}:")

    Q = int(input())
    for _ in range(Q):
        target_sum = int(input())
        left, right = 0, n-1
        ans = 0
        min_diff = float('inf')

        while left < right:
            diff = abs(target[left] + target[right] - target_sum)

            if diff < min_diff:
                min_diff = diff
                ans = target[left] + target[right]
            
            if target[left] + target[right] < target_sum:
                left += 1
            
            elif target[left] + target[right] > target_sum:
                right -= 1
            
            else:
                ans = target[left] + target[right]
                break
        
        print(f"Closest sum to {target_sum} is {ans}.")
    
    case += 1
