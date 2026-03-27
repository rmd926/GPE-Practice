import sys

tc = int(sys.stdin.readline())
for _ in range(tc):
    L, K = map(int, sys.stdin.readline().split())
  
    # 這邊測資會有亂七八糟的鬼東西，例如測資不會在同一行所以需要檢查是否有K個元素放到nums裡面
    target = []
    while len(target) < K:
        target.extend(map(int, sys.stdin.readline().split()))
    
    min_time, max_time = 0, 0
    # 公式解
    for num in target:
        min_time = max(min(num, L - num), min_time)
        max_time = max(max(num, L - num), max_time)
    print(min_time, max_time)
