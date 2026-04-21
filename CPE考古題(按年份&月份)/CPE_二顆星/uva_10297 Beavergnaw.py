import math
import sys

for line in sys.stdin:
    D, V = map(int, line.split())
    if D == 0 and V == 0:
        break
    d = (D**3 - 6*V/math.pi) ** (1/3)
    print(f"{d:.3f}")
