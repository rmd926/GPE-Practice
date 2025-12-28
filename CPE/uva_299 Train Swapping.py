def solution(target):
    count = 0
    for i in range(len(target)):
        for j in range(len(target)-i-1):
            if target[j] > target[j+1]:
                target[j], target[j+1] = target[j+1], target[j]
                count += 1
    return count

tc = int(input())
for i in range(tc):
    length = int(input())
    target = list(map(int, input().split()))
    count = solution(target)
    print(f"Optimal train swapping takes {count} swaps.")
