tc = 1

while True:
    n = int(input())
    if n == 0:
        break
    nums = []
    for _ in range(n):
        nums.append(int(input()))
    
    m = int(input())
    print(f"Case {tc}:")
    tc += 1

    for _ in range(m):
        target = int(input())
        min_diff = float("inf")

        
        for i in range(n):
            for j in range(i+1, n):
                temp = nums[i] + nums[j]

                if abs(target - temp) < min_diff:
                    min_diff = abs(target - temp)
                    ans = temp
        print(f"Closest sum to {target} is {ans}.")
