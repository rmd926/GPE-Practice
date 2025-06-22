import sys
import math

for line in sys.stdin:
    if not line.strip():
        continue

    S, D = map(int, line.strip().split())

    # 對應公式：
    # S + ceil( sqrt(4*S^2 + 8*D - 4*S + 1) / 2 - S - 0.5 )
    root_expr = math.sqrt(4 * S * S + 8 * D - 4 * S + 1)
    result = S + math.ceil(root_expr / 2 - S - 0.5)

    print(result)
