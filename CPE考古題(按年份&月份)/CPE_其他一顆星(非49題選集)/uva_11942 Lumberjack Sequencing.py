tc = int(input())
print("Lumberjacks:")
for _ in range(tc):
    try:
        target = list(map(int, input().split()))
    except:
        break
    
    if target == sorted(target) or target == sorted(target)[::-1]:
        print("Ordered")
    else:
        print("Unordered")

# 2026.05.26 輕鬆題，判斷是否降冪或升冪排列
