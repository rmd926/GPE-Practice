def calculate_distance(length, street_nums):
    street_nums.sort()
    mid = street_nums[length // 2]
    ans = 0
    for i in street_nums:
        ans += abs(i - mid)
    return ans


TC = int(input())
for _ in range(TC):
    target = list(map(int, input().split()))
    print(calculate_distance(target[0], target[1:]))