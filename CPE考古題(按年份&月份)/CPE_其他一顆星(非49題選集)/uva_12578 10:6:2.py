import math

tc = int(input())
for _ in range(tc):
    try:
        target = int(input())
    except:
        break

    width = target * 0.6
    r = target * 0.2

    circle_area = r ** 2 * math.pi
    rest_area = target * width - circle_area

    print(f"{circle_area:.2f} {rest_area:.2f}")
