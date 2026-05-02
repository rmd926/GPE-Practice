import math

while True:
    try:
        l, w, h, theta = map(float, input().split())
    except:
        break

    rad = math.radians(theta)

    if l * math.tan(rad) <= h:
        total = l * w * h
        empty = l * l * w * math.tan(rad) / 2
        ans = total - empty
    else:
        ans = h * h * w / (2 * math.tan(rad))

    print("{:.3f} mL".format(ans))
