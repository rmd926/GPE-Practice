import math
tc = 1
while True:
    try:
        v1, d1, v2, d2 = map(int, input().split())
    except:
        break

    if v1 == v2 == d1 == d2 == 0:
        break

    if d1 / v1 < d2 / v2:
        print(f"Case #{tc}: You owe me a beer!")
    elif d1 /v1 > d2 / v2:
        print(f"Case #{tc}: No beer for the captain.")
    
    temp1 = (d1 * v2 + d2 * v1)
    temp2 = v1 * v2 * 2
    gcd = math.gcd(temp1, temp2)

    if temp1 % temp2 == 0:
        ans = temp1 // temp2
    
    else:
        ans = f"{temp1//gcd}/{temp2//gcd}"
    
    print(f"Avg. arrival time: {ans}")

    tc += 1
