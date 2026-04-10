import math

'''
# triangle = (1/2) * r^2 * sin(theta)
# theta = (360/n) degree
'''
while True:
    try:
        r, n = map(eval, input().split())
    except:
        break

    theta = 2 * math.pi / n # pi = 180 degree
    ans = 0.5 * (r**2) * math.sin(theta) * n

    print(f"{ans:.3f}")
