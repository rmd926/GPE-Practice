while True:  
    target = int(input())        
    x, y = 1, 1                  # x 表示目前的對角線編號，y 表示該對角線最後一項的編號
    while y < target:            # 找出 target 所在的對角線
        x += 1                   # 對角線編號往下走
        y += x                   # 更新該對角線的最後一項編號 (因為第 x 條對角線有 x 個元素)

    p = 1 + y - target           # 計算在該對角線上的位置 (從尾端往回數)
    q = x - p + 1                # 另一個座標，透過公式算出來

    if x % 2 == 1:               # 如果對角線編號是奇數 → 從上往下
        print(f"TERM {target} IS {p}/{q}")
    else:                        # 如果對角線編號是偶數 → 從下往上
        print(f"TERM {target} IS {q}/{p}")
