import math

tc = int(input())
for _ in range(tc):
    target = list(map(int, input().split()))

    max_gcd = float('-inf')

    for i in range(len(target)-1):
        for j in range(i+1, len(target)):
            max_gcd = max(max_gcd, math.gcd(target[i], target[j]))
            
    print(max_gcd)
