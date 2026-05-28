import math
tc = int(input())
for t in range(tc):
    try:
        s1 = input()
        s2 = input()
    except:
        break
    num1 = int(s1, 2)
    num2 = int(s2, 2)

    if math.gcd(num1, num2) == 1:
        print(f"Pair #{t+1}: Love is not all you need!")
    else:
        print(f"Pair #{t+1}: All you need is love!")
