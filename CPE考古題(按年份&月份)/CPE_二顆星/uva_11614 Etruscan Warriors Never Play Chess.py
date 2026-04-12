# n^2 + n - 2 * target
# ans = (-1 + sqrt(8 * target + 1)) // 2 無條件捨去

tc = int(input())
for _ in range(tc):
    try:
        target = int(input())
    except:
        break
    
    ans = (-1 + (4 * 2 * target + 1) ** 0.5) // 2
    print(int(ans))
